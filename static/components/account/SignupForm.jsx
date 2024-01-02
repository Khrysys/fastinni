import Form from "../../blocks/Form";
import ThirdParty from "./ThirdParty";

export function SignupForm() {
    function onSubmit() {

    }

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