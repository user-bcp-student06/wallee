"""Andamiaje determinista de build para Wallee: NestJS (backend) y React + Vite (frontend).

Solo contiene archivos que no describen el feature. El código de aplicación
(módulos, controladores, servicios, componentes, rutas) lo genera el AI Engineer.
"""
import json
from pathlib import Path

BACKEND_DIR = "backend-nestjs"
FRONTEND_DIR = "frontend-react"


def _json(data: dict) -> str:
    return json.dumps(data, indent=2, ensure_ascii=False) + "\n"


BACKEND_PACKAGE_JSON = _json({
    "name": BACKEND_DIR,
    "version": "1.0.0",
    "private": True,
    "scripts": {
        "build": "nest build",
        "start": "nest start",
        "start:dev": "nest start --watch",
        "test": "jest",
        "test:e2e": "jest --config ./test/jest-e2e.json",
    },
    "dependencies": {
        "@nestjs/common": "^10.3.0",
        "@nestjs/core": "^10.3.0",
        "@nestjs/jwt": "^10.2.0",
        "@nestjs/platform-express": "^10.3.0",
        "@nestjs/typeorm": "^10.0.2",
        "bcryptjs": "^2.4.3",
        "better-sqlite3": "^11.1.2",
        "class-transformer": "^0.5.1",
        "class-validator": "^0.14.1",
        "pg": "^8.11.5",
        "reflect-metadata": "^0.2.2",
        "rxjs": "^7.8.1",
        "typeorm": "^0.3.20",
    },
    "devDependencies": {
        "@nestjs/cli": "^10.3.2",
        "@nestjs/schematics": "^10.1.1",
        "@nestjs/testing": "^10.3.0",
        "@types/bcryptjs": "^2.4.6",
        "@types/express": "^4.17.21",
        "@types/jest": "^29.5.12",
        "@types/node": "^20.12.7",
        "@types/supertest": "^6.0.2",
        "jest": "^29.7.0",
        "supertest": "^7.0.0",
        "ts-jest": "^29.1.2",
        "typescript": "^5.4.5",
    },
    "jest": {
        "moduleFileExtensions": ["js", "json", "ts"],
        "rootDir": "src",
        "testRegex": ".*\\.spec\\.ts$",
        "transform": {"^.+\\.ts$": "ts-jest"},
        "testEnvironment": "node",
    },
})

BACKEND_TSCONFIG_JSON = _json({
    "compilerOptions": {
        "module": "commonjs",
        "declaration": True,
        "removeComments": True,
        "emitDecoratorMetadata": True,
        "experimentalDecorators": True,
        "allowSyntheticDefaultImports": True,
        "esModuleInterop": True,
        "target": "ES2021",
        "sourceMap": True,
        "outDir": "./dist",
        "baseUrl": "./",
        "incremental": True,
        "skipLibCheck": True,
        "strictNullChecks": False,
        "noImplicitAny": False,
        "forceConsistentCasingInFileNames": True,
    },
})

BACKEND_TSCONFIG_BUILD_JSON = _json({
    "extends": "./tsconfig.json",
    "exclude": ["node_modules", "test", "dist", "**/*spec.ts"],
})

BACKEND_NEST_CLI_JSON = _json({
    "$schema": "https://json.schemastore.org/nest-cli",
    "collection": "@nestjs/schematics",
    "sourceRoot": "src",
})

BACKEND_JEST_E2E_JSON = _json({
    "moduleFileExtensions": ["js", "json", "ts"],
    "rootDir": ".",
    "testEnvironment": "node",
    "testRegex": ".e2e-spec.ts$",
    "transform": {"^.+\\.(t|j)s$": "ts-jest"},
})

BACKEND_MAIN_TS = """import { ValidationPipe } from '@nestjs/common';
import { NestFactory } from '@nestjs/core';
import { AppModule } from './app.module';

async function bootstrap() {
  const app = await NestFactory.create(AppModule);
  app.enableCors({ origin: ['http://localhost:5173', 'http://127.0.0.1:5173'] });
  app.useGlobalPipes(new ValidationPipe({ whitelist: true, forbidNonWhitelisted: true, transform: true }));
  await app.listen(process.env.PORT ?? 3000);
}
bootstrap();
"""

FRONTEND_PACKAGE_JSON = _json({
    "name": FRONTEND_DIR,
    "version": "1.0.0",
    "private": True,
    "type": "module",
    "scripts": {
        "dev": "vite",
        "build": "tsc --noEmit && vite build",
        "preview": "vite preview",
        "test": "vitest run",
    },
    "dependencies": {
        "react": "^18.3.1",
        "react-dom": "^18.3.1",
        "react-router-dom": "^6.23.1",
    },
    "devDependencies": {
        "@testing-library/dom": "^10.1.0",
        "@testing-library/jest-dom": "^6.4.6",
        "@testing-library/react": "^16.0.0",
        "@testing-library/user-event": "^14.5.2",
        "@types/react": "^18.3.3",
        "@types/react-dom": "^18.3.0",
        "@vitejs/plugin-react": "^4.3.1",
        "jsdom": "^24.1.0",
        "typescript": "^5.4.5",
        "vite": "^5.3.1",
        "vitest": "^1.6.0",
    },
})

FRONTEND_TSCONFIG_JSON = _json({
    "compilerOptions": {
        "target": "ES2020",
        "useDefineForClassFields": True,
        "lib": ["ES2020", "DOM", "DOM.Iterable"],
        "module": "ESNext",
        "skipLibCheck": True,
        "moduleResolution": "bundler",
        "resolveJsonModule": True,
        "isolatedModules": True,
        "noEmit": True,
        "jsx": "react-jsx",
        "strict": True,
        "types": ["vitest/globals"],
    },
    "include": ["src", "vite.config.ts"],
})

FRONTEND_VITE_CONFIG_TS = """import react from '@vitejs/plugin-react';
import { defineConfig } from 'vitest/config';

export default defineConfig({
  plugins: [react()],
  server: { port: 5173 },
  test: {
    environment: 'jsdom',
    globals: true,
    setupFiles: './src/setupTests.ts',
  },
});
"""

FRONTEND_INDEX_HTML = """<!doctype html>
<html lang="es">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>Wallee</title>
  </head>
  <body>
    <div id="root"></div>
    <script type="module" src="/src/main.tsx"></script>
  </body>
</html>
"""

FRONTEND_MAIN_TSX = """import React from 'react';
import ReactDOM from 'react-dom/client';
import { BrowserRouter } from 'react-router-dom';
import App from './App';
import './index.css';

ReactDOM.createRoot(document.getElementById('root') as HTMLElement).render(
  <React.StrictMode>
    <BrowserRouter>
      <App />
    </BrowserRouter>
  </React.StrictMode>,
);
"""

FRONTEND_INDEX_CSS = """* { box-sizing: border-box; margin: 0; padding: 0; }
body {
  font-family: system-ui, -apple-system, 'Segoe UI', sans-serif;
  min-height: 100vh;
}
"""

FRONTEND_VITE_ENV_D_TS = '/// <reference types="vite/client" />\n'
FRONTEND_SETUP_TESTS_TS = "import '@testing-library/jest-dom/vitest';\n"

SCAFFOLD_FILES = {
    BACKEND_DIR: {
        "package.json": BACKEND_PACKAGE_JSON,
        "tsconfig.json": BACKEND_TSCONFIG_JSON,
        "tsconfig.build.json": BACKEND_TSCONFIG_BUILD_JSON,
        "nest-cli.json": BACKEND_NEST_CLI_JSON,
        "test/jest-e2e.json": BACKEND_JEST_E2E_JSON,
        "src/main.ts": BACKEND_MAIN_TS,
    },
    FRONTEND_DIR: {
        "package.json": FRONTEND_PACKAGE_JSON,
        "tsconfig.json": FRONTEND_TSCONFIG_JSON,
        "vite.config.ts": FRONTEND_VITE_CONFIG_TS,
        "index.html": FRONTEND_INDEX_HTML,
        "src/main.tsx": FRONTEND_MAIN_TSX,
        "src/index.css": FRONTEND_INDEX_CSS,
        "src/vite-env.d.ts": FRONTEND_VITE_ENV_D_TS,
        "src/setupTests.ts": FRONTEND_SETUP_TESTS_TS,
    },
}

SCAFFOLD_LABELS = {BACKEND_DIR: "Backend NestJS", FRONTEND_DIR: "Frontend React + Vite"}


def ensure_scaffolding(output_dir: Path) -> None:
    """Escribe solo los archivos de build que falten; nunca pisa lo ya existente.

    No crea app.module.ts ni App.tsx: dependen del feature y los emite el AI
    Engineer. Si faltan, el proyecto queda incompleto a propósito: es la señal
    de que el paso falló, no algo que el andamiaje deba tapar.
    """
    for project, files in SCAFFOLD_FILES.items():
        created = 0
        for rel_path, content in files.items():
            file_path = Path(output_dir) / project / rel_path
            if not file_path.exists():
                file_path.parent.mkdir(parents=True, exist_ok=True)
                file_path.write_text(content, encoding="utf-8")
                created += 1
        if created:
            print(f"  🏗️ Scaffolding {SCAFFOLD_LABELS[project]}: generados {created} archivos base")
