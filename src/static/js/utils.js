function ready(callback) {
  window.addEventListener('load', callback);
}

ready(() => {
  console.log("It Works!");
})

export { ready }