import React from 'react'
import Home from './components/Home.js'
import Menu from './components/Menu.js'
import Login from './components/Login.js'
import CreateAccount from './components/CreateAccount.js'
import {
  BrowserRouter as Router,
  Switch,
  Route,
} from 'react-router-dom'
import './App.css';

class App extends React.Component {
  render() {
    return (
      <Router>
        <Menu/>
        <Switch>
          <Route path='/newuser'>
            <CreateAccount />
          </Route>
          <Route path='/login'>
            <Login/>
          </Route>
          <Route path='/'>
            <Home/>
          </Route>
        </Switch>
      </Router>
    )
  }
}

export default App;
