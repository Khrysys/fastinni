import { useContext } from "react";
import { isSigningUp, SignupProvider } from "../../general/AccountContext";
import "../scss/login.scss";
import { LoginForm } from "./account/LoginForm";
import { SignupForm } from "./account/SignupForm";

export default function LoginContainer() {
    return <div className="login-container">
        <SignupProvider>
            <FormSwitcher/>
        </SignupProvider>
    </div>
}

function FormSwitcher() {
    const {isSignup, setIsSignup} = useContext(isSigningUp)

    return <>
        {isSignup ? <SignupForm/> : <LoginForm/>}
        <button className='signup-toggle' onClick={() => setIsSignup(!isSignup)}>
            { isSignup ? 
                <a>Already have an account?</a> :
                <a>Don't have an account?</a> 
            }
        </button>
    </>
}