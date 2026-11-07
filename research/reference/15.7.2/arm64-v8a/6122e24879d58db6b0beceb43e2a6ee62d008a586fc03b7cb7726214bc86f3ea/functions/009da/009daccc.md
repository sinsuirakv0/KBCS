# 009daccc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

<!-- kbcs-version-next -->
**別版の対応** [v15.7.4 `009dad10`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009da/009dad10.md)
<!-- /kbcs-version-next -->

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
  "source_sha256": "05852a046441cc871d216dec7aee2490b4e5dd1875f36af17ed75096b9ff6c78",
  "source_text_sha256": "05852a046441cc871d216dec7aee2490b4e5dd1875f36af17ed75096b9ff6c78"
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

## 疑似コード / UTF-8 674 bytes

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
    _ZdlPv(local_48);
  }
  if ((local_40[0] & 1) != 0) {
    _ZdlPv(local_30);
  }
  if (*(long *)(lVar1 + 0x28) == local_28) {
    return;
  }
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~
