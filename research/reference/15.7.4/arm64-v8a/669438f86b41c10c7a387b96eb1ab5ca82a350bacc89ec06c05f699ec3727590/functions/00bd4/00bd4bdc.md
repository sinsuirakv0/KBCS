# 00bd4bdc

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

## 関数情報

~~~json
{
  "address": "00bd4bdc",
  "name": "FUN_00bd4bdc",
  "size": 272,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "570edd918c2461921137c50411a4b489531290bbcf8934cf488ade53c52030b3",
  "source_text_sha256": "570edd918c2461921137c50411a4b489531290bbcf8934cf488ade53c52030b3"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bd4d04](../00bd4/00bd4d04.md)
- [00bdd250](../00bdd/00bdd250.md)
- [00bde2c0](../00bde/00bde2c0.md)

## 疑似コード / UTF-8 2418 bytes

~~~c

void FUN_00bd4bdc(long param_1,undefined8 *param_2)

{
  ushort uVar1;
  ushort uVar2;
  ulong uVar3;
  void *__ptr;
  long *extraout_x1;
  long lVar4;
  size_t __size;
  
  if ((*(byte *)(param_1 + 0x1c) & 1) != 0) {
    return;
  }
                    /* catch(type#1 @ 00000000) { ... } // from try @ 00bd4af8 with catch @ 00bd4bf8
                       catch(type#1 @ 00000000) { ... } // from try @ 00bd4b28 with catch @ 00bd4bf8
                       catch(type#1 @ 00000000) { ... } // from try @ 00bd4b5c with catch @ 00bd4bf8
                       catch(type#1 @ 00000000) { ... } // from try @ 00bd4b88 with catch @ 00bd4bf8
                       catch(type#1 @ 00000000) { ... } // from try @ 00bd4bb0 with catch @ 00bd4bf8
                        */
                    /* try { // try from 00bd4bfc to 00cd4cff has its CatchHandler @ 00bd4bfc
                       catch() { ... } // from try @ 00bd4bfc with catch @ 00bd4bfc
                       catch() { ... } // from try @ 00bd4d08 with catch @ 00bd4bfc
                       catch() { ... } // from try @ 00bd4dbc with catch @ 00bd4bfc */
  *(undefined1 *)(param_1 + 0x1c) = 1;
  FUN_00bd4d04();
  if (extraout_x1 == (long *)0x0) goto LAB_00bd4cd0;
  uVar1 = *(ushort *)((long)extraout_x1 + 9);
  uVar2 = uVar1 >> 8 & 3;
  if (uVar2 == 0) {
LAB_00bd4c70:
    lVar4 = param_2[1];
    __ptr = (void *)*param_2;
    if ((ulong)param_2[2] < lVar4 + 1U) {
      __size = param_2[2] * 2;
      uVar3 = lVar4 + 0x3e1;
      if (__size < uVar3 || __size - uVar3 == 0) {
        __size = uVar3;
      }
      param_2[2] = __size;
      __ptr = realloc(__ptr,__size);
      *param_2 = __ptr;
      if (__ptr == (void *)0x0) {
                    /* WARNING: Subroutine does not return */
        abort();
      }
      lVar4 = param_2[1];
    }
    *(undefined1 *)((long)__ptr + lVar4) = 0x29;
    param_2[1] = param_2[1] + 1;
  }
  else {
    if (uVar2 == 2) {
      uVar3 = (**(code **)(*extraout_x1 + 8))(extraout_x1,param_2);
      if ((uVar3 & 1) != 0) goto LAB_00bd4c70;
      uVar1 = *(ushort *)((long)extraout_x1 + 9);
    }
    if (((uVar1 >> 10 & 3) == 0) ||
       (((uVar1 >> 10 & 3) == 2 &&
        (uVar3 = (**(code **)(*extraout_x1 + 0x10))(extraout_x1,param_2), (uVar3 & 1) != 0))))
    goto LAB_00bd4c70;
  }
  (**(code **)(*extraout_x1 + 0x28))(extraout_x1,param_2);
LAB_00bd4cd0:
  *(undefined1 *)(param_1 + 0x1c) = 0;
  return;
}

~~~
