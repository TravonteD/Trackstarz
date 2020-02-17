import axios from 'axios'

axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";
axios.defaults.xsrfCookieName = "csrftoken";

export const api = {
  authenticate(username, password) {
    axios({
      method: 'GET',
      url:'http://127.0.0.1:8000/main/users',
      responseType: 'json'
    })
      .then((response) => {
        console.log(response.body)
      })
    // if (this.getAuthentication()) {
    //   this.toggleState()
    //   return
    // }

  },
  toggleState() {
    this.isAuthenticated = !this.isAuthenticated
  },
  getAuthentication() {
  }

}

