import { useEffect } from "react";
import Form from "../../blocks/Form";
import ThirdParty from "./ThirdParty";
import { ajax } from "jquery";

export function SignupForm() {
    function onSubmit() {

    }

    // This gets the CSRF header info for this form
    useEffect(() => {
        ajax(location.origin + "/api/latest/account/signup").done(function(response) {
            console.log(response)
        })
    }, [])

    return <>
        <header>
            <a>
                <b>Login to Fastinni</b>
            </a>
        </header>
        <Form onSubmit={() => onSubmit()}>
            <ThirdParty/>
        </Form>

    </>
}