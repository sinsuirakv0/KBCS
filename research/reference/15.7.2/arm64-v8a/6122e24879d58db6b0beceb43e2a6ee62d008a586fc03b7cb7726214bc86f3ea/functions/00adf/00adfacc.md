# 00adfacc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00adfacc.md)

## 関数情報

~~~json
{
  "address": "00adfacc",
  "name": "FUN_00adfacc",
  "size": 224,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "b8cfe1a1f92677f7507b403a0abffe8429b3bdfc9927ff3a0a35c796a6ad2e18",
  "source_text_sha256": "b8cfe1a1f92677f7507b403a0abffe8429b3bdfc9927ff3a0a35c796a6ad2e18"
}
~~~
## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00444c54](../00444/00444c54.md)
- [0044592c](../00445/0044592c.md)
- [00467c58](../00467/00467c58.md)
- [00886014](../00886/00886014.md)
- [00bdb6c0](../00bdb/00bdb6c0.md)

## 疑似コード 1/1 / UTF-8 1600 bytes

~~~c

void FUN_00adfacc(undefined8 param_1,undefined8 *param_2,undefined8 *param_3)

{
  int iVar1;
  int iVar2;
  long lVar3;
  int extraout_var;
  int extraout_w1;
  int extraout_var_00;
  undefined8 uVar4;
  undefined8 uVar5;
  undefined8 uVar6;
  
                    /* try { // try from 00adfad0 to 00bdfad7 has its CatchHandler @ 00adfc30 */
  uVar4 = *param_3;
  uVar5 = *param_2;
                    /* try { // try from 00adfaec to 00bdfb0b has its CatchHandler @ 00adfc0c */
  FUN_00444c54(uVar4,0xbe,0xbe,0xbe,0xff);
                    /* try { // try from 00adfb20 to 00bdfb23 has its CatchHandler @ 00adfc30 */
  lVar3 = __dynamic_cast(DAT_00c249b8,&PTR_PTR_00be8d98,&PTR_PTR_00be8da8,0);
  uVar6 = *(undefined8 *)(lVar3 + 0x38);
  iVar1 = FUN_00886014(uVar5);
                    /* try { // try from 00adfb38 to 00bdfb3f has its CatchHandler @ 00adfc00 */
  FUN_00886014(uVar5);
                    /* try { // try from 00adfb54 to 00bdfb5b has its CatchHandler @ 00adfbfc */
  lVar3 = __dynamic_cast(DAT_00c249b8,&PTR_PTR_00be8d98,&PTR_PTR_00be8da8,0);
  iVar2 = FUN_00467c58(*(undefined8 *)(lVar3 + 0x38));
  FUN_00886014(uVar5);
                    /* try { // try from 00adfb70 to 00bdfb77 has its CatchHandler @ 00adfc00 */
  FUN_00886014(uVar5);
                    /* try { // try from 00adfb8c to 00bdfb93 has its CatchHandler @ 00adfbe4 */
                    /* try { // try from 00adfba8 to 00bdfbab has its CatchHandler @ 00adfc00 */
  FUN_0044592c(uVar4,uVar6,(extraout_w1 + iVar1) - iVar2,extraout_var_00 + extraout_var,0);
  return;
}

~~~
