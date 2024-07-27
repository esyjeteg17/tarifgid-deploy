import { defineStore } from "pinia";
import { useRouter } from "vue-router";
import { useNuxtApp } from "#app";

export const useAuthStore = defineStore("auth", {
  state: () => ({
    token: null,
    user: null,
  }),
  actions: {
    getToken() {
      return this.token;
    },
    setToken(token) {
      this.token = token;
    },
    setUser(user) {
      this.user = user;
    },
    logout() {
      this.token = null;
      this.user = null;
      const router = useRouter();
      router.push("/login");
    },
    async fetchUser() {
      if (this.token) {
        const { $api } = useNuxtApp();
        try {
          const { data } = await $api.get("http://127.0.0.1:8000/api/user/", {
            headers: {
              Authorization: `Bearer ${this.token}`,
            },
          });
          this.setUser(data);
        } catch (error) {
          console.error(error);
          this.logout();
        }
      }
    },
  },
});
