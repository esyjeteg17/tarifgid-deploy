export default ($api) => ({
  async login(credentials) {
    const { data } = await $api.post(
      "http://127.0.0.1:8000/api/token/",
      credentials
    );
    return data;
  },
  async register(user) {
    const { data } = await $api.post(
      "http://127.0.0.1:8000/api/register/",
      user
    );
    return data;
  },
  async refreshToken(refreshToken) {
    const { data } = await $api.post(
      "http://127.0.0.1:8000/api/token/refresh/",
      {
        refresh: refreshToken,
      }
    );
    return data;
  },
});
