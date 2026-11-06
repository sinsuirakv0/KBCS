# 00bbaab4

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

## 関数情報

~~~json
{
  "address": "00bbaab4",
  "name": "FUN_00bbaab4",
  "size": 292,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "d5ac710da9b9a8d8f95bd4b7134ae17adb839666a464949512e725ac44a2670b",
  "source_text_sha256": "d5ac710da9b9a8d8f95bd4b7134ae17adb839666a464949512e725ac44a2670b"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bbb19c](../00bbb/00bbb19c.md)
- [00bbb4c0](../00bbb/00bbb4c0.md)
- [00bd4fd8](../00bd4/00bd4fd8.md)
- [00bd4fe4](../00bd4/00bd4fe4.md)
- [00be1de0](../00be1/00be1de0.md)
- [00be1e30](../00be1/00be1e30.md)

## 関連文字列（未確認候補）

~~~text
"terminating"
"terminating due to %s exception of type %s"
"terminating due to %s exception of type %s: %s"
"terminating due to %s foreign exception"
"uncaught"
~~~

## 疑似コード / UTF-8 4423 bytes

~~~c

void FUN_00bbaab4(void)

{
  undefined *puVar1;
  long *plVar2;
  ulong uVar3;
  long lVar4;
  undefined8 uVar5;
  long lVar6;
  long lVar7;
  long *local_18;
  
                    /* catch() { ... } // from try @ 00bb56cc with catch @ 00bbaab8 */
                    /* catch() { ... } // from try @ 00bb9e30 with catch @ 00bbaabc */
  plVar2 = (long *)__cxa_get_globals_fast();
                    /* catch() { ... } // from try @ 00bb9e24 with catch @ 00bbaad0 */
  if ((plVar2 == (long *)0x0) || (lVar6 = *plVar2, lVar6 == 0)) {
                    /* catch() { ... } // from try @ 00bb9ec0 with catch @ 00bbaad8 */
                    /* WARNING: Subroutine does not return */
    FUN_00bbb19c("terminating");
  }
  uVar3 = FUN_00bd4fe4(lVar6 + 0x60);
                    /* catch() { ... } // from try @ 00bb9eb0 with catch @ 00bbaaec */
  if ((uVar3 & 1) == 0) {
                    /* catch() { ... } // from try @ 00bb9a78 with catch @ 00bbab24 */
                    /* WARNING: Subroutine does not return */
    FUN_00bbb19c("terminating due to %s foreign exception",PTR_s_uncaught_00c249a0);
  }
                    /* catch() { ... } // from try @ 00bb9a00 with catch @ 00bbaaf4 */
  lVar4 = FUN_00bd4fd8(lVar6 + 0x60);
                    /* catch() { ... } // from try @ 00bb99f4 with catch @ 00bbab08 */
  if (lVar4 == 0x434c4e47432b2b01) {
                    /* catch() { ... } // from try @ 00bb9a88 with catch @ 00bbab10 */
    local_18 = *(long **)(lVar6 + 8);
  }
  else {
                    /* catch() { ... } // from try @ 00bba4d4 with catch @ 00bbab2c */
    local_18 = (long *)(lVar6 + 0x80);
  }
                    /* catch() { ... } // from try @ 00bb5630 with catch @ 00bbab30 */
  lVar7 = *(long *)(lVar6 + 0x10);
                    /* catch() { ... } // from try @ 00bb7c1c with catch @ 00bbab34 */
                    /* catch() { ... } // from try @ 00bb5544 with catch @ 00bbab38 */
                    /* catch() { ... } // from try @ 00bb552c with catch @ 00bbab3c */
                    /* catch() { ... } // from try @ 00bb551c with catch @ 00bbab40 */
                    /* catch() { ... } // from try @ 00bb3514 with catch @ 00bbab44 */
  lVar6 = *(long *)(lVar7 + 8);
                    /* catch() { ... } // from try @ 00bba014 with catch @ 00bbab48 */
                    /* catch() { ... } // from try @ 00bb9c90 with catch @ 00bbab4c */
  lVar4 = __cxa_demangle(lVar6,0,0,0);
                    /* catch() { ... } // from try @ 00bb9c84 with catch @ 00bbab60 */
                    /* catch() { ... } // from try @ 00bb9bd8 with catch @ 00bbab68 */
                    /* catch() { ... } // from try @ 00bb9bcc with catch @ 00bbab6c */
  if (lVar4 != 0) {
    lVar6 = lVar4;
  }
                    /* catch() { ... } // from try @ 00bb98bc with catch @ 00bbab70 */
                    /* catch() { ... } // from try @ 00bb98c8 with catch @ 00bbab78 */
  uVar3 = (**(code **)(*(long *)PTR__ZTISt9exception_00c1ae88 + 0x20))
                    (PTR__ZTISt9exception_00c1ae88,lVar7,&local_18);
  puVar1 = PTR_s_uncaught_00c249a0;
  if ((uVar3 & 1) != 0) {
    uVar5 = (**(code **)(*local_18 + 0x10))();
                    /* catch() { ... } // from try @ 00bb7674 with catch @ 00bbabac */
                    /* catch() { ... } // from try @ 00bb72c4 with catch @ 00bbabb0 */
                    /* catch() { ... } // from try @ 00bb6f10 with catch @ 00bbabb4 */
                    /* catch() { ... } // from try @ 00bb6b5c with catch @ 00bbabb8 */
                    /* WARNING: Subroutine does not return */
                    /* catch() { ... } // from try @ 00bb67a8 with catch @ 00bbabbc */
    FUN_00bbb19c("terminating due to %s exception of type %s: %s",puVar1,lVar6,uVar5);
  }
                    /* catch() { ... } // from try @ 00bb63f4 with catch @ 00bbabc0 */
                    /* catch() { ... } // from try @ 00bb6040 with catch @ 00bbabc4 */
                    /* catch() { ... } // from try @ 00bb5c80 with catch @ 00bbabc8 */
                    /* catch() { ... } // from try @ 00bb58c0 with catch @ 00bbabcc */
                    /* catch() { ... } // from try @ 00bb5148 with catch @ 00bbabd0 */
                    /* WARNING: Subroutine does not return */
                    /* catch() { ... } // from try @ 00bb4d68 with catch @ 00bbabd4 */
  FUN_00bbb19c("terminating due to %s exception of type %s",PTR_s_uncaught_00c249a0,lVar6);
}

~~~
