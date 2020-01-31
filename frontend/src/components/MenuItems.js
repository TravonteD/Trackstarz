import React from 'react';

function MenuItems(props) {
  let list = []
  for (let i of props.items) {
    list.push(<li className="mainmenu__item nav-item">{i.toUpperCase()}</li>)
  }
  return (list)
}

export default MenuItems;
