# 00b0eedc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

## 関数情報

~~~json
{
  "address": "00b0eedc",
  "name": "FUN_00b0eedc",
  "size": 188,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "83d494677ea9d2a50c34e7e2af8816b4290d3d2047311d39162a3438e5e1941b",
  "source_text_sha256": "83d494677ea9d2a50c34e7e2af8816b4290d3d2047311d39162a3438e5e1941b"
}
~~~

## 呼び出し元

- [00a223d0](../00a22/00a223d0.md)

## 呼び出し先

- [00480d48](../00480/00480d48.md)
- [00480e28](../00480/00480e28.md)

## 疑似コード / UTF-8 696 bytes

~~~c

void FUN_00b0eedc(undefined4 *param_1,undefined8 param_2)

{
  FUN_00480e28(param_2,*param_1);
  FUN_00480e28(param_2,param_1[3]);
  FUN_00480e28(param_2,param_1[5]);
  FUN_00480e28(param_2,param_1[4]);
  FUN_00480e28(param_2,param_1[1]);
  FUN_00480e28(param_2,*(undefined1 *)(param_1 + 7));
  FUN_00480e28(param_2,*(undefined1 *)((long)param_1 + 0x1d));
  FUN_00480e28(param_2,*(undefined1 *)((long)param_1 + 0x1e));
  FUN_00480e28(param_2,*(undefined1 *)((long)param_1 + 0x1f));
  FUN_00480e28(param_2,param_1[2]);
  FUN_00480e28(param_2,*(undefined1 *)(param_1 + 8));
  FUN_00480e28(param_2,*(undefined1 *)(param_1 + 9));
  FUN_00480d48(param_2,*(undefined1 *)(param_1 + 0xb));
  return;
}

~~~
