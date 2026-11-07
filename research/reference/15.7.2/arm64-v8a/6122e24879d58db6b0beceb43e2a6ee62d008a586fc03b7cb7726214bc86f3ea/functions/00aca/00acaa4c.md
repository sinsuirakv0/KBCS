# 00acaa4c

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

<!-- kbcs-version-next -->
**別版の対応** [v15.7.4 `00acab58`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aca/00acab58.md)
<!-- /kbcs-version-next -->

## 関数情報

~~~json
{
  "address": "00acaa4c",
  "name": "FUN_00acaa4c",
  "size": 160,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "64e42402d3fce5d38b79094d3adacec480a48dd0c23114704866fd103801921e",
  "source_text_sha256": "64e42402d3fce5d38b79094d3adacec480a48dd0c23114704866fd103801921e"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bdaf60](../00bda/00bdaf60.md)

## 疑似コード / UTF-8 858 bytes

~~~c

void FUN_00acaa4c(undefined8 *param_1)

{
  long lVar1;
  void *__ptr;
  long lVar2;
  
  lVar1 = param_1[1];
  lVar2 = param_1[2];
  do {
    if (lVar2 == lVar1) {
      if ((void *)*param_1 != (void *)0x0) {
        _ZdlPv((void *)*param_1);
        return;
      }
      return;
    }
    param_1[2] = lVar2 + -0x60;
    if ((*(byte *)(lVar2 + -0x18) & 1) == 0) {
      if ((*(byte *)(lVar2 + -0x30) & 1) == 0) goto LAB_00acaa8c;
LAB_00acaaa8:
      _ZdlPv(*(void **)(lVar2 + -0x20));
      __ptr = *(void **)(lVar2 + -0x48);
    }
    else {
      _ZdlPv(*(void **)(lVar2 + -8));
      if ((*(byte *)(lVar2 + -0x30) & 1) != 0) goto LAB_00acaaa8;
LAB_00acaa8c:
      __ptr = *(void **)(lVar2 + -0x48);
    }
    if (__ptr != (void *)0x0) {
      *(void **)(lVar2 + -0x40) = __ptr;
      _ZdlPv(__ptr);
    }
    lVar2 = param_1[2];
  } while( true );
}

~~~
