# 006dabac

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

## 関数情報

~~~json
{
  "address": "006dabac",
  "name": "FUN_006dabac",
  "size": 408,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "4062b819a8bbce9188351d2b798942bec33776733938e238c5ddae50c9bdb8b0",
  "source_text_sha256": "4062b819a8bbce9188351d2b798942bec33776733938e238c5ddae50c9bdb8b0"
}
~~~

## 呼び出し元

- [006dad74](../006da/006dad74.md)

## 呼び出し先

- [00440ec0](../00440/00440ec0.md)
- [0048791c](../00487/0048791c.md)
- [0048793c](../00487/0048793c.md)
- [006f9ed8](../006f9/006f9ed8.md)
- [00c57e90](../00c57/00c57e90.md)
- [00c57eb0](../00c57/00c57eb0.md)
- [00c58000](../00c58/00c58000.md)

## 疑似コード / UTF-8 3206 bytes

~~~c

void FUN_006dabac(undefined4 *param_1,long *param_2)

{
  ulong uVar1;
  ulong *puVar2;
  ulong *puVar3;
  undefined4 uVar4;
  int iVar5;
  ulong uVar6;
  long lVar7;
  void *__dest;
  undefined8 *puVar8;
  ulong uVar9;
  ulong uVar10;
  int iVar11;
  void *__src;
  ulong *puVar12;
  long lVar13;
  
  puVar8 = (undefined8 *)(param_1 + 2);
                    /* try { // try from 006dabb0 to 007dabf7 has its CatchHandler @ 006daf20 */
  *puVar8 = 0;
  *(undefined8 *)(param_1 + 4) = 0;
  *(undefined8 *)(param_1 + 6) = 0;
  FUN_0048791c(param_2);
  uVar4 = FUN_0048793c(param_2,0);
                    /* try { // try from 006dabf8 to 007dac0b has its CatchHandler @ 006daf0c */
  *param_1 = uVar4;
  uVar4 = FUN_0048793c(param_2,1);
  param_1[1] = uVar4;
  *(undefined8 *)(param_1 + 4) = *(undefined8 *)(param_1 + 2);
  FUN_0048791c(param_2);
  iVar11 = 0;
  do {
                    /* try { // try from 006dac40 to 007dac47 has its CatchHandler @ 006daef8 */
    iVar5 = (**(code **)(*param_2 + 0x28))(param_2);
    if (iVar5 <= iVar11) {
                    /* try { // try from 006dad28 to 007dad3b has its CatchHandler @ 006daed0 */
      return;
    }
    uVar6 = FUN_0048793c(param_2,iVar11);
    lVar7 = FUN_0048793c(param_2,iVar11 + 1);
    puVar3 = *(ulong **)(param_1 + 4);
    if (puVar3 < *(ulong **)(param_1 + 6)) {
      puVar12 = puVar3 + 1;
      *puVar3 = uVar6 & 0xffffffff | lVar7 << 0x20;
    }
    else {
                    /* try { // try from 006dac80 to 007dac87 has its CatchHandler @ 006daee4 */
      __src = (void *)*puVar8;
      lVar13 = (long)puVar3 - (long)__src >> 3;
                    /* try { // try from 006dac90 to 007dac97 has its CatchHandler @ 006daec0 */
      uVar1 = lVar13 + 1;
      if (uVar1 >> 0x3d != 0) {
        FUN_006f9ed8(puVar8);
LAB_006dad40:
                    /* WARNING: Subroutine does not return */
                    /* try { // try from 006dad40 to 007dad77 has its CatchHandler @ 006daeec */
        FUN_00440ec0();
      }
      uVar9 = (long)*(ulong **)(param_1 + 6) - (long)__src;
      uVar10 = (long)uVar9 >> 2;
                    /* try { // try from 006daca8 to 007dacb7 has its CatchHandler @ 006daeb8 */
      if (uVar10 <= uVar1) {
        uVar10 = uVar1;
      }
                    /* try { // try from 006dacb8 to 007dacc7 has its CatchHandler @ 006daeb4 */
      if (0x7ffffffffffffff7 < uVar9) {
        uVar10 = 0x1fffffffffffffff;
      }
      if (uVar10 == 0) {
        __dest = (void *)0x0;
      }
      else {
        if (uVar10 >> 0x3d != 0) goto LAB_006dad40;
        __dest = (void *)_Znwm(uVar10 << 3);
      }
      puVar2 = (ulong *)((long)__dest + lVar13 * 8);
                    /* try { // try from 006dacf4 to 007dad07 has its CatchHandler @ 006daeac */
      puVar12 = puVar2 + 1;
      *puVar2 = uVar6 & 0xffffffff | lVar7 << 0x20;
      memcpy(__dest,__src,(long)puVar3 - (long)__src);
      *(void **)(param_1 + 2) = __dest;
      *(ulong **)(param_1 + 4) = puVar12;
      *(void **)(param_1 + 6) = (void *)((long)__dest + uVar10 * 8);
      if (__src != (void *)0x0) {
        _ZdlPv(__src);
      }
    }
    *(ulong **)(param_1 + 4) = puVar12;
    iVar11 = iVar11 + 2;
  } while( true );
}

~~~
