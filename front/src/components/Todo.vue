<template>
  <div id="todo">
    <label v-for="label in options" :key="label.label">
      <input type="radio" v-model="current" v-bind:value="label.value" />{{
        label.label
      }}
    </label>

    ( {{ computedTodos.length }} )

    <table>
      <thead v-pre>
        <tr>
          <th class="status">Status</th>
          <th class="task">Task</th>
          <th class="button"></th>
        </tr>
      </thead>
      <tbody>
        <tr
          v-for="item in computedTodos"
          v-bind:key="item.id"
          v-bind:class="{ done: item.state }"
        >
          <td class="status">
            <button v-on:click="doChangeState(item)">
              {{ labels[item.state] }}
            </button>
          </td>
          <td class="task">{{ item.task }}</td>
          <td class="button">
            <button v-on:click="doRemove(item)">Delete</button>
          </td>
        </tr>
      </tbody>
    </table>

    <h2>New Task</h2>
    <form class="add-form" v-on:submit.prevent="doAdd">
      Task <input type="text" ref="comment" />
      <button type="submit">Add</button>
    </form>
  </div>
</template>

<script>
import Cookies from "js-cookie";

export default {
  name: "Todo",

  data() {
    return {
      todos: [],
      current: -1,
      options: [
        { value: -1, label: "All" },
        { value: 0, label: "Working" },
        { value: 1, label: "Done" },
      ],
      csrf: "",
    };
  },
  computed: {
    computedTodos: function () {
      return this.todos.filter((el) => {
        return this.current < 0 ? true : this.current === el.state;
      }, this);
    },

    labels() {
      return this.options.reduce(function (a, b) {
        return Object.assign(a, { [b.value]: b.label });
      }, {});
    },
  },

  created() {
    this.todos = [];
    this.getTodo(this.todos);
  },

  methods: {
    getTodo: function (todos) {
      fetch(`/api/items/`)
        .then((res) => res.json())
        .then((res) => {
          res.map((x) => {
            x.deleted
              ? ""
              : todos.push({
                  ...x,
                  state: x.done ? 1 : 0,
                });
          });
        });
    },

    doAdd: function () {
      const comment = this.$refs.comment;
      if (!comment.value.length) {
        return;
      }
      const csrfToken = Cookies.get("csrftoken");
      const body = {
        task: comment.value,
      };
      fetch(`/api/items/`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          "X-CSRFToken": csrfToken,
        },
        body: JSON.stringify(body),
      })
        .then((res) => res.json())
        .then((res) => {
          this.todos.push({
            ...res,
            state: 0,
          });
          comment.value = "";
        });
    },

    doChangeState: function (item) {
      const csrfToken = Cookies.get("csrftoken");
      fetch(`/api/items/${item.id}/`, {
        method: "PUT",
        headers: {
          "Content-Type": "application/json",
          "X-CSRFToken": csrfToken,
        },
        body: JSON.stringify({ done: item.done ? false : true }),
      }).then(() => {
        item.done = item.done ? false : true;
        item.state = item.state ? 0 : 1;
      });
    },

    doRemove: function (item) {
      const csrfToken = Cookies.get("csrftoken");
      fetch(`/api/items/${item.id}/`, {
        method: "PUT",
        headers: {
          "Content-Type": "application/json",
          "X-CSRFToken": csrfToken,
        },
        body: JSON.stringify({ deleted: true }),
      });
      var index = this.todos.indexOf(item);
      this.todos.splice(index, 1);
    },
  },
};
</script>

<style scoped>
* {
  box-sizing: border-box;
}
div {
  max-width: 600px;
  margin: 0 auto;
}
table {
  width: 100%;
  border-collapse: collapse;
}
thead th {
  border-bottom: 2px solid #7ccf56; /*#d31c4a */
  color: #7ccf56; /* #0099e4 */
}
th,
th {
  padding: 0 8px;
  line-height: 40px;
}
thead th.status {
  width: 100px;
}
thead th.button {
  width: 60px;
}
tbody td.button,
tbody td.done,
tbody td.status {
  text-align: center;
}
tbody tr td,
tbody tr th {
  border-bottom: 1px solid #ccc;
  transition: all 0.4s;
  text-align: left;
}
tbody tr.done td,
tbody tr.done th {
  background: #f8f8f8;
  color: #bbb;
}
tbody tr:hover td,
tbody tr:hover th {
  background: #f4fbff;
}
button {
  border: none;
  border-radius: 20px;
  line-height: 24px;
  padding: 0 8px;
  background: #7ccf56;
  color: #fff;
  cursor: pointer;
}
</style>
