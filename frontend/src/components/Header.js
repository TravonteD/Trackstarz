import React from 'react';
import logo from '../images/New-Logo-All-White-Wide.png';
import Menu from './Menu.js';

function Header() {
  return (
    <header className='trackstarz__header navbar navbar-expand-lg'>
    <div className='container-fluid'>
    <div className='navbar-header'>
    <img className='trackstarz__header--img' src={ logo } alt={'logo'}/>
    </div>
    <Menu/>
    </div>
    </header>
  )
}

export default Header;
