# jeux-de-quebec-a24

## Recommended IDE Setup

[VSCode](https://code.visualstudio.com/) + [Volar](https://marketplace.visualstudio.com/items?itemName=Vue.volar) (and disable Vetur).

## Customize configuration

See [Vite Configuration Reference](https://vitejs.dev/config/).

## Project Setup

## Data
A `.env` file at the root of `server` with a Spoonacular API key is necessary to use the app.
```
SPOONACULAR_API_KEY = <Your API key>
```

A CSV file containing data from the Open Food Facts database is also necessary. The file path needs to be assigned to the constant `OFF_EXPORT_PATH` in `server/main.py`

The necessary attribution text for the use of data from the two sources at the time of writing is already present in the UI.

### Server Setup

1. Navigate to the `/server` directory:
     ```bash
     cd server
     ```

2. Create a Virtual Environment using `venv`:
     ```bash
     python -m venv venv
     ```

3. Activate the Virtual Environment:
     ```bash
     source venv/bin/activate  # On Windows: ./venv/Scripts/activate
     ```

4. Install Required Packages:
     ```bash
     pip install -r requirements.txt
     ```

5. Run the Server:
   - Start the server using the main Python file:
     ```bash
     python main.py
     ```
   - The server will run at [`localhost:5000`](http://localhost:5000).
   - You can check the server health at [`localhost:5000/health`](http://localhost:5000/health)
   
### UI Setup

1. Navigate to the `/ui` directory:
     ```bash
     cd ui
     ```

2. Install Required Packages:
     ```bash
     npm install
     ```

3. Run the UI in Development Mode (with Hot-Reloading):
     ```bash
     npm run dev
     ```
     - The UI will run at [`localhost:5173`](http://localhost:5173).

4. Production Build:
     ```bash
     npm run build
     ```
