import React from 'react';
import MenuItems from './MenuItems.js'

function Menu() {
  return (
    <React.Fragment>
    <button 
      type='button'
      className='navbar-toggler'
      data-toggle='collapse'
      data-target='#navbarSupportedContent'
      aria-controls='navbarSupportedContent'
      aria-expanded='false'
      aria-label='Toggle navigation'>
    </button>
    <div 
      className='mainmenu collapse navbar-collapse' 
      id='navbarSupportedContent'>
        <nav className='navbar-nav'>
          <MenuItems items={
            {
              '/newuser': 'newuser',
              '/login': 'login',
              '/': 'home'
              // '/about': 'about', 
              // '/universe': 'universe',
              // '/jaidot': 'jaidot',
              // '/nectar': 'nectar',
              // '/merch': 'merch',
              // '/contact': 'contact',
            }
          }/>
        </nav>
      </div>
    </React.Fragment>
  )
}

export default Menu;
