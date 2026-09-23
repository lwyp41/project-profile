# Technical Architecture

## Goal and applicability

Recover boundaries, runtime, interfaces, integrations, deterministic components, and deployment evidence. File structure is not proof of scale or reliability.

## Investigation by depth

- **Brief:** inspect entry point, manifest, and top-level architecture documentation.
- **Standard:** inspect modules, APIs, configuration, scripts, tests, and integrations.
- **Deep:** trace runtime/deployment, data flow, failure paths, dependency history, and deterministic validation boundaries.

## Facts, interview, and rendering

Record component, interface, runtime, dependency, source, and limitation. Ask only about material runtime/deployment facts unavailable in artifacts. Do not infer production use from a package; render boundaries and evidence limits.

## Render by depth

- **Brief render:** system boundary, entry/runtime, and 1–2 core components.
- **Standard render:** preserve Brief; add component relationships, core runtime or data path, major interfaces/integrations, one consequential constraint or choice, and an important limitation where evidenced.
- **Deep render:** preserve Standard; add architecture layers/boundaries, runtime plus data/control flow, failure or degradation paths, deterministic validation boundaries, consequential rationale, material evolution, conflicts, and unresolved evidence limits where evidenced.
