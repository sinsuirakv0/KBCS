# 009daccc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](009daccc.md)

## 関数情報

~~~json
{
  "address": "009daccc",
  "name": "FUN_009daccc",
  "size": 148,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "fa9db29c7f78b5c6527577221178e11dcc50365a2d1a0d07fadb8dfc803c5d93",
  "source_text_sha256": "fa9db29c7f78b5c6527577221178e11dcc50365a2d1a0d07fadb8dfc803c5d93"
}
~~~
## 呼び出し元

- [0060b7bc](../0060b/0060b7bc.md)
- [007317b0](../00731/007317b0.md)

## 呼び出し先

- [0053f81c](../0053f/0053f81c.md)
- [009daa10](../009da/009daa10.md)
- [00bdaf60](../00bda/00bdaf60.md)
- [00bdaf90](../00bda/00bdaf90.md)

## 疑似コード 1/1 / UTF-8 726 bytes

~~~c

void FUN_009daccc(undefined8 param_1)

{
  long lVar1;
  byte local_58 [16];
  void *local_48;
  byte local_40 [16];
  void *local_30;
  long local_28;
  
  lVar1 = tpidr_el0;
  local_28 = *(long *)(lVar1 + 0x28);
  FUN_009daa10(local_40);
  local_58[5] = 0;
  local_58[0] = 8;
  local_58[1] = 0x3c;
  local_58[2] = 0x62;
  local_58[3] = 0x72;
  local_58[4] = 0x3e;
  FUN_0053f81c(param_1,local_40,local_58);
  if ((local_58[0] & 1) != 0) {
    operator_delete(local_48);
  }
  if ((local_40[0] & 1) != 0) {
    operator_delete(local_30);
  }
  if (*(long *)(lVar1 + 0x28) == local_28) {
    return;
  }
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~
