import React from 'react';
import { Link } from 'react-router-dom';

function MenuItems(props) {
  let list = []
  for (let i in props.items) {
    list.push(<li key={i} className="mainmenu__item nav-item"><Link className='mainmenu__item--link' to={i}>{props.items[i].toUpperCase()}</Link></li>)
  }
  return (list)
}

export default MenuItems;
