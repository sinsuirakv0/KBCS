# 00adf9fc

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

## 関数情報

~~~json
{
  "address": "00adf9fc",
  "name": "FUN_00adf9fc",
  "size": 284,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "04dcc758f7687751d0ece695b02abd7fd04f201fc81bd29e73a4077730969695",
  "source_text_sha256": "04dcc758f7687751d0ece695b02abd7fd04f201fc81bd29e73a4077730969695"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00419064](../00419/00419064.md)
- [00457e1c](../00457/00457e1c.md)
- [00459efc](../00459/00459efc.md)
- [0081f580](../0081f/0081f580.md)
- [00885f80](../00885/00885f80.md)
- [00add7d4](../00add/00add7d4.md)
- [00bdaff0](../00bda/00bdaff0.md)

## 疑似コード / UTF-8 2744 bytes

~~~c

void FUN_00adf9fc(undefined8 param_1,undefined8 *param_2,int *param_3)

{
  int iVar1;
  undefined8 uVar2;
  long lVar3;
  long lVar4;
  undefined8 *puVar5;
  undefined8 *puVar6;
  long *plVar7;
  undefined8 *puVar8;
  undefined8 *puVar9;
  
                    /* try { // try from 00adf9fc to 00bdfa1b has its CatchHandler @ 00adfc58 */
  if (*param_3 == 5) {
                    /* try { // try from 00adfa4c to 00bdfa53 has its CatchHandler @ 00adfc38 */
    lVar3 = FUN_0081f580();
    lVar4 = FUN_0081f580();
    iVar1 = *(int *)(lVar4 + 0x2290);
    puVar6 = *(undefined8 **)(lVar3 + 0x2280);
    if (*(undefined8 **)(lVar3 + 0x2280) == (undefined8 *)0x0) {
                    /* try { // try from 00adfa68 to 00bdfa6b has its CatchHandler @ 00adfc44 */
      puVar8 = (undefined8 *)(lVar3 + 0x2280);
      puVar9 = (undefined8 *)(lVar3 + 0x2280);
    }
    else {
      do {
        while( true ) {
                    /* try { // try from 00adfa80 to 00bdfa87 has its CatchHandler @ 00adfc30 */
          puVar5 = puVar6;
          puVar8 = puVar5;
          if (iVar1 < *(int *)((long)puVar5 + 0x1c)) break;
          if (iVar1 <= *(int *)((long)puVar5 + 0x1c)) goto LAB_00adfaf0;
                    /* try { // try from 00adfa98 to 00bdfa9f has its CatchHandler @ 00adfc14 */
          puVar6 = (undefined8 *)puVar5[1];
          if ((undefined8 *)puVar5[1] == (undefined8 *)0x0) {
            puVar9 = puVar5 + 1;
            goto LAB_00adfaa4;
          }
        }
        puVar6 = (undefined8 *)*puVar5;
        puVar9 = puVar5;
      } while ((undefined8 *)*puVar5 != (undefined8 *)0x0);
    }
LAB_00adfaa4:
    puVar5 = (undefined8 *)_Znwm(0x70);
    *puVar5 = 0;
    puVar5[1] = 0;
                    /* try { // try from 00adfab4 to 00bdfabb has its CatchHandler @ 00adfc0c */
    puVar5[2] = puVar8;
    *puVar9 = puVar5;
    plVar7 = *(long **)(lVar3 + 0x2278);
    *(int *)((long)puVar5 + 0x1c) = iVar1;
                    /* try { // try from 00adfad0 to 00bdfad7 has its CatchHandler @ 00adfc30 */
    puVar6 = puVar5;
    if (*plVar7 != 0) {
      *(long *)(lVar3 + 0x2278) = *plVar7;
      puVar6 = (undefined8 *)*puVar9;
    }
    FUN_00419064(*(undefined8 *)(lVar3 + 0x2280),puVar6);
                    /* try { // try from 00adfaec to 00bdfb0b has its CatchHandler @ 00adfc0c */
    *(long *)(lVar3 + 0x2288) = *(long *)(lVar3 + 0x2288) + 1;
LAB_00adfaf0:
    FUN_00add7d4(puVar5 + 4);
    lVar3 = FUN_0081f580();
    *(undefined4 *)(lVar3 + 0x2290) = 0xffffffff;
  }
  else if (*param_3 == 2) {
    FUN_00885f80(*param_2);
    uVar2 = FUN_00457e1c();
                    /* try { // try from 00adfa30 to 00bdfa37 has its CatchHandler @ 00adfc44 */
    FUN_00459efc(uVar2,0xb,0);
    return;
  }
  return;
}

~~~
