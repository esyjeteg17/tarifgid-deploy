import axios from "axios";

export default defineNuxtPlugin((nuxtApp) => {
  const api = axios.create({
    baseURL: nuxtApp.$config.public.apiBase,
  });

  return {
    provide: {
      api,
    },
  };
});
