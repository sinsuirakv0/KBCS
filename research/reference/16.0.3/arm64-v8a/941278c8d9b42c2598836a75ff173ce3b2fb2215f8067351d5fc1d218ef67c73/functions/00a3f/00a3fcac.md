# 00a3fcac

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "00a3fcac",
  "name": "FUN_00a3fcac",
  "size": 184,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "891c5fed07ef7a62a7e4a73a02d5c44b3e7a8c8f8612702893034d5e20e44085",
  "source_text_sha256": "891c5fed07ef7a62a7e4a73a02d5c44b3e7a8c8f8612702893034d5e20e44085"
}
~~~

## 呼び出し元

- [00a3f914](../00a3f/00a3f914.md)
- [00a3f968](../00a3f/00a3f968.md)

## 呼び出し先

- [0043be80](../0043b/0043be80.md)
- [00691c08](../00691/00691c08.md)

## 疑似コード / UTF-8 873 bytes

~~~c

void FUN_00a3fcac(undefined8 *param_1,undefined8 *param_2)

{
  undefined8 uVar1;
  undefined8 uVar2;
  
  *param_1 = *param_2;
  if ((*(byte *)(param_2 + 1) & 1) == 0) {
    uVar2 = param_2[2];
    uVar1 = param_2[1];
    param_1[3] = param_2[3];
    param_1[2] = uVar2;
    param_1[1] = uVar1;
  }
  else {
    FUN_0043be80(param_1 + 1,param_2[3],param_2[2]);
  }
  param_1[5] = 0;
  param_1[4] = param_1 + 5;
  param_1[6] = 0;
                    /* catch() { ... } // from try @ 00a3dd3c with catch @ 00a3fd18 */
  FUN_00691c08(param_1 + 4,param_2[4],param_2 + 5);
                    /* catch() { ... } // from try @ 00a3dcf0 with catch @ 00a3fd30 */
  param_1[8] = 0;
  param_1[7] = param_1 + 8;
                    /* catch() { ... } // from try @ 00a3dd00 with catch @ 00a3fd38 */
  param_1[9] = 0;
  FUN_00691c08(param_1 + 7,param_2[7],param_2 + 8);
  return;
}

~~~
