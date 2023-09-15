import "./css/header.css";
import "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.2/css/all.min.css";

import { Component } from "react";

export class Header extends Component {
    constructor(props) {
        super(props);
        this.state = {
            isResponsive: false,
        }
    }

    toggleResponsiveNavigation() {
        this.state.isResponsive = !this.state.isResponsive
    }

    render() {
        var classes = "topnav";
        if(this.state.isResponsive) {
            classes += " responsive";
        }
        return <div class={classes} id="myTopnav">
            <a href="#home" class="active">Home</a>
            <a href="#news">News</a>
            <a href="#contact">Contact</a>
            <a href="#about">About</a>
            <a class="icon" onclick={ this.toggleResponsiveNavigation}>
                <i class="fa fa-bars"></i>
            </a>
        </div>
    }
}