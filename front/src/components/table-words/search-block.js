import React from 'react'
import '../../styles/search-block.css'

export default class SearchBlock extends React.Component {
  constructor () {
    super()
    this.AddFocus = this.AddFocus.bind(this)
        // this.DeleteFocus = this.DeleteFocus.bind(this);
  }

  AddFocus (e) {
    e.target.focus()
  }

    // DeleteFocus(e) {
    //     e.target.blur()
    // }

  render () {
    return (
      <div className='search-block'>
        <input
          type='text'
          onChange={this.props.onChange}
          placeholder='Search words...'
          onMouseEnter={this.AddFocus}
          /* onMouseOut={this.DeleteFocus} */
        />
      </div>
    )
  }
}
