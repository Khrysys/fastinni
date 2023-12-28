export default function Form({onSubmit, children}) {
    return <form onKeyDown={
			(e) => {
				/**
				 * Note: Pressing enter in some input in a browser forms
				 *  triggers onClick on the first child button
				 *
				 * So, prevent `enter` from triggering `onClick` on any buttons
				 *  and instead trigger onSubmit
				 */
				if (e.key === 'Enter') {
					e.preventDefault();
					onSubmit();
				}
			}
		}

		onSubmit={
			(e) => {
				/**
				 * Prevent submit from reloading the page
				 */
				e.preventDefault();
				e.stopPropagation();
				onSubmit();
			}
		}>
		{children}
	</form>
}