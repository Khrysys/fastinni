import { Form } from "../blocks/Form";
import { ThirdPartyLogin } from "./ThirdPartyLogin";

export function SignupForm() {
    return <div className="signup-form">
        < Form >
            <input type="text" required data-val-length="Username length cannot be longer than 64 characters." data-val-length-max="64" placeholder="Username" id="username" name="username"/>
            <input type="password" required placeholder="Password" id="password" name="password"/>
            <input type="password" required placeholder="Verify Password" id="password_confirm" name="password_match"/>
            <input type="text" placeholder="Email" id="email" name="email"/>
            <input type="checkbox" id="email_2fa" name="email"/>
            <label for="email_2fa">Enable Two Factor Authentication for Email</label>
            <input type="text" placeholder="Phone Number" id="phone" name="phone"/>
            <input type="checkbox" id="phone_2fa" name="phone_2fa"/>
            <label for="phone_2fa">Enable Two Factor Authentication for Phone</label>
            <input type="checkbox" id="remember"/>
            <label htmlFor="remember">Remember Me</label>
            <input type="submit" value="Submit"/>
            < ThirdPartyLogin />
        </Form>
        
    </div>
}