import { useState } from "react"
import "../../css/login.css"
import { LoginForm } from "./LoginForm";
import { SignupForm } from "./SignupForm";


export function LoginContainer() {
    const [isNewAccount, setIsNewAccount] = useState(false);

    return <div className="login-container">
        {isNewAccount ? < SignupForm /> : < LoginForm />}
        <button className="signup-toggle" onClick={() => setIsNewAccount(!isNewAccount)}>{isNewAccount ? "Already have an account?" : "Don't have an account?"}</button>
    </div>
}