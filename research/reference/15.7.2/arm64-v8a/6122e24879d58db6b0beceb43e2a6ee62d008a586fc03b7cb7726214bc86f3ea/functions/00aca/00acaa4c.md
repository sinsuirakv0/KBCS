# 00acaa4c

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00acaa4c.md)

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
  "source_sha256": "4599b365a1ac6a2a984df482261ec714e44d06138d6693677745572fb2989a03",
  "source_text_sha256": "4599b365a1ac6a2a984df482261ec714e44d06138d6693677745572fb2989a03"
}
~~~
## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bdaf60](../00bda/00bdaf60.md)

## 疑似コード 1/1 / UTF-8 939 bytes

~~~c

void FUN_00acaa4c(undefined8 *param_1)

{
  long lVar1;
  void *pvVar2;
  long lVar3;
  
  lVar1 = param_1[1];
  lVar3 = param_1[2];
  do {
    if (lVar3 == lVar1) {
      if ((void *)*param_1 != (void *)0x0) {
        operator_delete((void *)*param_1);
        return;
      }
      return;
    }
    param_1[2] = lVar3 + -0x60;
    if ((*(byte *)(lVar3 + -0x18) & 1) == 0) {
      if ((*(byte *)(lVar3 + -0x30) & 1) == 0) goto LAB_00acaa8c;
LAB_00acaaa8:
      operator_delete(*(void **)(lVar3 + -0x20));
      pvVar2 = *(void **)(lVar3 + -0x48);
    }
    else {
      operator_delete(*(void **)(lVar3 + -8));
      if ((*(byte *)(lVar3 + -0x30) & 1) != 0) goto LAB_00acaaa8;
LAB_00acaa8c:
      pvVar2 = *(void **)(lVar3 + -0x48);
    }
    if (pvVar2 != (void *)0x0) {
      *(void **)(lVar3 + -0x40) = pvVar2;
      operator_delete(pvVar2);
    }
    lVar3 = param_1[2];
  } while( true );
}

~~~
