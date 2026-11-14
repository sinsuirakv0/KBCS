# 00aca6ec

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "00aca6ec",
  "name": "FUN_00aca6ec",
  "size": 244,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "5e64074fff561147f3a22e79b20931296e40b99026e35dc8110766298caaa051",
  "source_text_sha256": "5e64074fff561147f3a22e79b20931296e40b99026e35dc8110766298caaa051"
}
~~~

## 呼び出し元

- [00839a78](../00839/00839a78.md)
- [008c0858](../008c0/008c0858.md)
- [008d3aa4](../008d3/008d3aa4.md)
- [008d970c](../008d9/008d970c.md)
- [008dac04](../008da/008dac04.md)
- [008fe500](../008fe/008fe500.md)
- [00a3de60](../00a3d/00a3de60.md)
- [00ac0514](../00ac0/00ac0514.md)
- [00ac9524](../00ac9/00ac9524.md)

## 呼び出し先

- [008524fc](../00852/008524fc.md)
- [008b7f1c](../008b7/008b7f1c.md)
- [008b89cc](../008b8/008b89cc.md)

## 疑似コード / UTF-8 1573 bytes

~~~c

void FUN_00aca6ec(long param_1)

{
  long lVar1;
  undefined8 uVar2;
  
                    /* try { // try from 00aca6f4 to 00bca703 has its CatchHandler @ 00acaaf0 */
  lVar1 = FUN_008524fc();
  lVar1 = FUN_008b89cc(lVar1 + 0x2f38,*(undefined4 *)(param_1 + 4));
  if (lVar1 != 0) {
    lVar1 = FUN_008524fc();
    uVar2 = FUN_008b89cc(lVar1 + 0x2f38,*(undefined4 *)(param_1 + 4));
    FUN_008b7f1c(uVar2,1);
  }
                    /* try { // try from 00aca730 to 00bca743 has its CatchHandler @ 00acaae8 */
  lVar1 = FUN_008524fc();
  lVar1 = FUN_008b89cc(lVar1 + 0x2f38,*(undefined4 *)(param_1 + 8));
  if (lVar1 != 0) {
    lVar1 = FUN_008524fc();
    uVar2 = FUN_008b89cc(lVar1 + 0x2f38,*(undefined4 *)(param_1 + 8));
    FUN_008b7f1c(uVar2,1);
  }
                    /* try { // try from 00aca764 to 00bca777 has its CatchHandler @ 00acab08 */
  lVar1 = FUN_008524fc();
  lVar1 = FUN_008b89cc(lVar1 + 0x2f38,*(undefined4 *)(param_1 + 0xc));
  if (lVar1 != 0) {
                    /* try { // try from 00aca77c to 00bca7af has its CatchHandler @ 00acab28 */
    lVar1 = FUN_008524fc();
    uVar2 = FUN_008b89cc(lVar1 + 0x2f38,*(undefined4 *)(param_1 + 0xc));
    FUN_008b7f1c(uVar2,1);
  }
  lVar1 = FUN_008524fc();
  lVar1 = FUN_008b89cc(lVar1 + 0x2f38,*(undefined4 *)(param_1 + 0x10));
  if (lVar1 != 0) {
    lVar1 = FUN_008524fc();
                    /* try { // try from 00aca7b8 to 00bca7bf has its CatchHandler @ 00acab40 */
    uVar2 = FUN_008b89cc(lVar1 + 0x2f38,*(undefined4 *)(param_1 + 0x10));
    FUN_008b7f1c(uVar2,1);
    return;
  }
  return;
}

~~~
