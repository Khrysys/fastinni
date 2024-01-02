import { isSignupForm } from "../contexts/AccountContext";
import "../css/login.css";
import { LoginForm } from "./account/LoginForm";
import { SignupForm } from "./account/SignupForm";

export default function LoginContainer() {
    return <div className="login-container">
        <isSignupProvider>
            <FormSwitcher/>
        </isSignupProvider>
        
    </div>
}

function FormSwitcher() {
    const {isSignup, setIsSignup} = useContext(isSignupForm)

    return <>
        {isSignup ? <SignupForm/> : <LoginForm/>}
        <button className='signup-toggle' onClick={setIsSignup(!isSignup)}>
            { isSignup ? 
                <a>Already have an account?</a> :
                <a>Don't have an account?</a> }
        </button>
    </>
}