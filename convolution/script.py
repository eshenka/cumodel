import json

cpu_operations = 20
gpu_operations = 48 - cpu_operations

model = {
    "variables": {
        "size": {
            "type": "usize"
        },
        "sum_size": {
            "type": "usize"
        },
        "W_size": {
            "type": "usize"
        },
        "S0_size": {
            "type": "usize"
        },
        "S1_size": {
            "type": "usize"
        },
        "X_size": {
            "type": "usize"
        },
        "X1_size": {
            "type": "usize"
        },
        "X2_size": {
            "type": "usize"
        },

        "Fs": {
            "type": "i32"
        },
        "L": {
            "type": "i32"
        },
        "M": {
            "type": "i32"
        },
        "p": {
            "type": "i32"
        },

        "S_0": {
            "type": "pointer"
        },
        "S_1": {
            "type": "pointer"
        },

        "a": {
            "type": "i32"
        },
        "b": {
            "type": "i32"
        },

        "A": {
            "type": "f32"
        },

        "X": {
            "type": "pointer"
        },
        "X1": {
            "type": "pointer"
        },
        "X2": {
            "type": "pointer"
        },
        "W": {
            "type": "pointer"
        },
        "B": {
            "type": "pointer"
        },
        "C": {
            "type": "pointer"
        },
        "X2PC": {
            "type": "pointer"
        },

        "X_raw": {
            "type": "pointer"
        },
        "opora": {
            "type": "pointer"
        },
        "N": {
            "type": "i32"
        },

        "meta": {
            "type": "pointer"
        },
        "meta_size": {
            "type": "usize"
        }

    },

    "operations": {
        "parse_opora": {
            "inputs": [
                "opora",
                "N"
            ],
            "outputs": [
                "Fs",
                "L",
                "M",
                "p",
                "S_0",
                "S0_size",
                "meta",
                "meta_size"

            ],
            "module": {
                "name": "c_parse_opora",
                "args": [
                    "opora",
                    "N",
                    "Fs",
                    "L",
                    "M",
                    "p",
                    "S_0",
                    "S0_size"
                    "meta",
                    "meta_size"
                ]
            }
        },

        "calc_coeff": {
            "inputs": [
                "S_0",
                "S0_size",
                "L"
            ],
            "outputs": [
                "a",
                "b",
                "A"
            ],
            "module": {
                "name": "c_calc_coeff",
                "args": [
                    "S_0",
                    "S0_size",
                    "L",
                    "a",
                    "b",
                    "A"
                ]
            }
        },
        "cu_calc_coeff": {
            "inputs": [
                "S_0",
                "S0_size",
                "L"
            ],
            "outputs": [
                "a",
                "b",
                "A"
            ],
            "module": {
                "name": "cuda_calc_coeff",
                "args": [
                    "S_0",
                    "S0_size",
                    "L",
                    "a",
                    "b",
                    "A"
                ]
            }
        },
        "calc_exps": {
            "inputs": [
                "M",
                "p"
            ],
            "outputs": [
                "W",
                "W_size"
            ],
            "module": {
                "name": "c_calc_exps",
                "args": [
                    "M",
                    "p",
                    "W",
                    "W_size"
                ]
            }
        },
        "cu_calc_exps": {
            "inputs": [
                "M",
                "p"
            ],
            "outputs": [
                "W",
                "W_size"
            ],
            "module": {
                "name": "cuda_calc_exps",
                "args": [
                    "M",
                    "p",
                    "W",
                    "W_size"
                ]
            }
        },
        "fft_i": {
            "inputs": [
                "S_0",
                "S0_size",
                "W",
                "W_size",
                "M",
                "p"
            ],
            "outputs": [
                "S_1",
                "S1_size"
            ],
            "module": {
                "name": "c_fft_i",
                "args": [
                    "S_0",
                    "S0_size",
                    "W",
                    "W_size",
                    "M",
                    "p",
                    "S_1",
                    "S1_size"
                ]
            }
        },
        "cu_fft_i": {
            "inputs": [
                "S_0",
                "S0_size",
                "W",
                "W_size",
                "M",
                "p"
            ],
            "outputs": [
                "S_1",
                "S1_size"
            ],
            "module": {
                "name": "cuda_fft_i",
                "args": [
                    "S_0",
                    "S0_size",
                    "W",
                    "W_size",
                    "M",
                    "p",
                    "S_1",
                    "S1_size"
                ]
            }
        },
    },

    "modules": {
        "c_parse_opora": {
            "function": "c_parse_opora",
            "device": "host",
        },

        "c_calc_coeff": {
            "function": "c_calc_coeff",
            "device": "host"
        },
        "cuda_calc_coeff": {
            "function": "cuda_calc_coeff",
            "device": "cuda"
        },

        "c_calc_exps": {
            "function": "c_calc_exps",
            "device": "host"
        },
        "cuda_calc_exps": {
            "function": "cuda_calc_exps",
            "device": "cuda"
        },

        "c_fft_i": {
            "function": "c_fft_i",
            "device": "host"
        },
        "cuda_fft_i": {
            "function": "cuda_fft_i",
            "device": "cuda"
        },

        "c_extract_samples": {
            "function": "c_extract_samples",
            "device": "host"
        },
        "cuda_extract_samples": {
            "function": "cuda_extract_samples",
            "device": "cuda"
        },

        "c_fft_multconj_rfft": {
            "function": "c_fft_multconj_rfft",
            "device": "host"
        },
        "cuda_fft_multconj_rfft": {
            "function": "cuda_fft_multconj_rfft",
            "device": "cuda"
        },

        "c_calc_output_trace": {
            "function": "c_calc_output_trace",
            "device": "host"
        },
        "cuda_calc_output_trace": {
            "function": "cuda_calc_output_trace",
            "device": "cuda"
        },

        "c_make_pc": {
            "function": "c_make_pcf",
            "device": "host"
        },
        "cuda_make_pc": {
            "function": "cuda_make_pcf",
            "device": "cuda"
        }
    }
}

for i in range(cpu_operations):
    operation_name = f"extract_samples_{i}"
    model['operations'][operation_name] = {
            "inputs": [
                f"X_raw_{i}",
                f"X_raw_{i}_size",
                "M",
                "Fs"
            ],
            "outputs": [
                f"X_{i}",
                f"X_{i}_size",
            ],
            "module": {
                "name": "c_extract_samples",
                "args": [
                    f"X_raw_{i}",
                    f"X_raw_{i}_size",
                    "M",
                    "Fs",
                    f"X_{i}",
                    f"X_{i}_size",
                ]
            }
        }
    
    model['variables'][f"X_raw_{i}"] = {"type": "pointer"}
    model['variables'][f"X_raw_{i}_size"] = {"type": "usize"}
    model['variables'][f"X_{i}"] = {"type": "pointer"}
    model['variables'][f"X_{i}_size"] = {"type": "usize"}

for i in range(gpu_operations):
    operation_name = f"cu_extract_samples_{i}"
    model['operations'][operation_name] = {
            "inputs": [
                f"X_raw_{i}",
                f"X_raw_{i}_size",
                "M",
                "Fs"
            ],
            "outputs": [
                f"X_{i}",
                f"X_{i}_size"
            ],
            "module": {
                "name": "cuda_extract_samples",
                "args": [
                    f"X_raw_{i}",
                    f"X_raw_{i}_size"
                    "M",
                    "Fs",
                    f"X_{i}",
                    f"X_{i}_size"
                ]
            }
        }

    model['variables'][f"X_raw_{i}"] = {"type": "pointer"}
    model['variables'][f"X_raw_{i}_size"] = {"type": "usize"}
    model['variables'][f"X_{i}"] = {"type": "pointer"}
    model['variables'][f"X_{i}_size"] = {"type": "usize"}

for i in range(cpu_operations):
    operation_name = f"fft_multconj_rfft_{i}"
    model['operations'][operation_name] = {
            "inputs": [
                f"X_{i}",
                f"X_{i}_size",
                "W",
                "W_size",
                "S_1",
                "S1_size",
                "M",
                "p"
            ],
            "outputs": [
                f"X1_{i}",
                f"X1_{i}_size"
            ],
            "module": {
                "name": "c_fft_multconj_rfft",
                "args": [
                    f"X_{i}",
                    f"X_{i}_size",
                    "W",
                    "W_size",
                    "S_1",
                    "S1_size",
                    "M",
                    "p",
                    f"X1_{i}"
                    f"X1_{i}_size"
                ]
            }
        }

    model['variables'][f"X1_{i}"] = {"type": "pointer"}
    model['variables'][f"X1_{i}_size"] = {"type": "usize"}

for i in range(gpu_operations):
    operation_name = f"cu_fft_multconj_rfft_{i}"
    model['operations'][operation_name] = {
            "inputs": [
                f"X_{i}",
                f"X_{i}_size",
                "W",
                "W_size",
                "S_1",
                "S1_size",
                "M",
                "p"
            ],
            "outputs": [
                f"X1_{i}",
                f"X1_{i}_size"
            ],
            "module": {
                "name": "cuda_fft_multconj_rfft",
                "args": [
                    f"X_{i}",
                    f"X_{i}_size",
                    "W",
                    "W_size",
                    "S_1",
                    "S1_size",
                    "M",
                    "p",
                    f"X1_{i}",
                    f"X1_{i}_size"
                ]
            }
        }
    model['variables'][f"X1_{i}"] = {"type": "pointer"}
    model['variables'][f"X1_{i}_size"] = {"type": "usize"}

for i in range(cpu_operations):
    operation_name = f"calc_output_trace_{i}"
    model['operations'][operation_name] = {
            "inputs": [
                f"X1_{i}",
                f"X1_{i}_size",
                "L",
                "a",
                "b"
            ],
            "outputs": [
                f"B_{i}",
                f"C_{i}",
                f"X2_{i}",
                f"X2_{i}_size"
            ],
            "module": {
                "name": "c_calc_output_trace",
                "args": [
                    f"X1_{i}",
                    f"X1_{i}_size",
                    "L",
                    "a",
                    "b",
                    f"B_{i}",
                    f"C_{i}",
                    f"X2_{i}",
                    f"X2_{i}_size"
                ]
            }
        }

    model['variables'][f"X2_{i}"] = {"type": "pointer"}
    model['variables'][f"X2_{i}_size"] = {"type": "usize"}
    model['variables'][f"B_{i}"] = {"type": "f32"}
    model['variables'][f"C_{i}"] = {"type": "f32"}

for i in range(gpu_operations):
    operation_name = f"cu_calc_output_trace{i}"
    model['operations'][operation_name] = {
            "inputs": [
                f"X1_{i}",
                "L",
                "a",
                "b"
            ],
            "outputs": [
                f"B_{i}",
                f"C_{i}",
                f"X2_{i}",
                f"X2_{i}_size"
            ],
            "module": {
                "name": "cuda_calc_output_trace",
                "args": [
                    f"X1_{i}",
                    "L",
                    "a",
                    "b",
                    f"B_{i}",
                    f"C_{i}",
                    f"X2_{i}",
                    f"X2_{i}_size"
                ]
            }
        }
    model['variables'][f"X2_{i}"] = {"type": "pointer"}
    model['variables'][f"X2_{i}_size"] = {"type": "usize"}
    model['variables'][f"B_{i}"] = {"type": "f32"}
    model['variables'][f"C_{i}"] = {"type": "f32"}

for i in range(cpu_operations):
    operation_name = f"make_pc_{i}"
    model['operations'][operation_name] = {
            "inputs": [
                f"X2_{i}",
                f"X2_{i}_size",
                f"B_{i}",
                f"C_{i}",
                "L",
                "meta",
                "meta_size"
            ],
            "outputs": [
                f"X2PC_{i}",
                f"X2PC_{i}_size"
            ],
            "module": {
                "name": "c_make_pc",
                "args": [
                    f"X2_{i}",
                    f"X2_{i}_size",
                    f"B_{i}",
                    f"C_{i}",
                    "L",
                    "meta",
                    f"X2PC_{i}"
                ]
            }
        }
    model['variables'][f"X2PC_{i}"] = {"type": "pointer"}
    model['variables'][f"X2PC_{i}_size"] = {"type": "usize"}

for i in range(gpu_operations):
    operation_name = f"cu_make_pc_{i}"
    model['operations'][operation_name] = {
            "inputs": [
                f"X2_{i}",
                f"X2_{i}_size",
                f"B_{i}",
                f"C_{i}",
                "L",
                "meta"
            ],
            "outputs": [
                f"X2PC_{i}",
                f"X2PC_{i}_size"
            ],
            "module": {
                "name": "cuda_make_pc",
                "args": [
                    f"X2_{i}",
                    f"B_{i}",
                    f"C_{i}",
                    "L",
                    "meta",
                    f"X2PC_{i}",
                    f"X2PC_{i}_size"
                ]
            }
        }

    model['variables'][f"X2PC_{i}"] = {"type": "pointer"}
    model['variables'][f"X2PC_{i}_size"] = {"type": "usize"}
    

    for operation_name, operation in model["operations"].items():
        args = []

        for input_name in operation.get("inputs", []):
            args.append({
                "type": model['variables'][input_name]['type'],
                "kind": "input",
            })

        for output_name in operation.get("outputs", []):
            args.append({
                "type": model['variables'][output_name]['type'],
                "kind": "output",
            })

        model['modules'][operation['module']['name']]['args'] = args

    

with open("generated_model.json", "w") as f:
    json.dump(model, f, indent=4)