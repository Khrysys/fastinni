import { useContext, useState } from "react";
import { Form } from "../blocks/Form";
import { ThirdPartyLogin } from "./ThirdPartyLogin";
import { ajax } from "jquery";
import { ErrorDispachContext } from "../../contexts/ErrorContext";

export function SignupForm() {
    const [tag, setTag] = useState("");
    const [tagMessage, setTagMessage] = useState("");
    const [usenameMessageType, setUsernameMessageType] = useState("")
    const setError = useContext(ErrorDispachContext);

    function onSubmit() {

    }

    function checkUsernameAvailibility() {
        ajax(process.env.NPM_API_URL + 'account/tag-available/' + tag + '/').done(function(data) {
            setTagMessage(data.responseJSON().availibilityMessage)
            setTagMessageType(data.responseJSON())
        }).fail(function(error) {
            setError(error.responseJSON().detail)
        })
    }

    return <div className="signup-form">
        <header>
            <a>
                <b>Create a New Fastinni Account</b>
            </a>
        </header>
        < Form onSubmit={onSubmit}>
            <input type="text" required data-val-length="Username length cannot be longer than 64 characters." data-val-length-max="64" placeholder="Username" id="username" name="username" value={username} onChange={e => setUsername(e.target.value)} onBlur={e => {checkUsernameAvailibility(() => checkUsernameAvailibility())}}/>
            <input type="password" required placeholder="Password" id="password" name="password"/>
            <input type="password" required placeholder="Verify Password" id="password_confirm" name="password_match"/>
            <input type="text" placeholder="Email" id="email" name="email"/>
            <input type="checkbox" id="email_2fa" name="email"/>
            <label for="email_2fa">Enable Two Factor Authentication for Email</label>
            <input type="text" placeholder="Phone Number" id="phone" name="phone"/>
            <input type="checkbox" id="phone_2fa" name="phone_2fa"/>
            <label for="phone_2fa">Enable Two Factor Authentication for Phone</label><br />
            <input type="checkbox" id="remember"/>
            <label htmlFor="remember">Remember Me</label>
            <input type="submit" value="Submit"/>
            < ThirdPartyLogin />
        </Form>
        
    </div>
}