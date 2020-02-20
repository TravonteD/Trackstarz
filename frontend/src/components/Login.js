import React from 'react'
import Header from './Header.js'
import { Link } from 'react-router-dom'
import { api } from '../Api.js'

function Login() {
  return (
    <div className='app'>
      <Header/>
      <React.Fragment>
        <div className='container'>
          <div className='form-group login-form col-sm-12 col-lg-4'>
            <h1 
              className='login-form__title'
                >LOGIN</h1>
            <input 
              className='form-control login-form__input' 
              type='text' 
              id='login-form--username' 
              name='username' 
              placeholder='username' />
            <input 
              className='form-control login-form__input' 
              type='password' 
              id='login-form--password' 
              name='password' 
              placeholder='password' />
            <button 
              className='btn btn-primary login-form__btn' 
              onClick={login}
              type='submit'>
              LOGIN
            </button>
            <p>Dont Have a login?</p>
            <button 
              className='btn btn-primary login-form__btn' 
              type='button'>
              <Link to='/newuser'>CREATE ACCOUNT</Link>
            </button>
          </div>
        </div>
      </React.Fragment>
    </div>
  )

  function login() {
    const username = document.getElementById('login-form--username').value
    const password = document.getElementById('login-form--password').value
    api.authenticate(username, password)
  }
}


export default Login;
