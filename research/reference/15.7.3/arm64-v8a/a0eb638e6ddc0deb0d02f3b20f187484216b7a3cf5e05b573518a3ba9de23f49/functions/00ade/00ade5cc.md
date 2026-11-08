# 00ade5cc

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

## 関数情報

~~~json
{
  "address": "00ade5cc",
  "name": "FUN_00ade5cc",
  "size": 300,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "325a1147245a724d47bf8b7fa5a42857b4b62b08d0ddffcae75896e76df716fb",
  "source_text_sha256": "325a1147245a724d47bf8b7fa5a42857b4b62b08d0ddffcae75896e76df716fb"
}
~~~

## 呼び出し元

- [005a79d8](../005a7/005a79d8.md)
- [005e144c](../005e1/005e144c.md)
- [0065040c](../00650/0065040c.md)
- [00653214](../00653/00653214.md)
- [006a8e60](../006a8/006a8e60.md)
- [0071b5e0](../0071b/0071b5e0.md)
- [0078cd14](../0078c/0078cd14.md)
- [0079bdf0](../0079b/0079bdf0.md)
- [007acf88](../007ac/007acf88.md)
- [007dfc70](../007df/007dfc70.md)
- [007e855c](../007e8/007e855c.md)
- [007e8848](../007e8/007e8848.md)
- [007f226c](../007f2/007f226c.md)
- [007f24c4](../007f2/007f24c4.md)
- [007f534c](../007f5/007f534c.md)
- [007f8b0c](../007f8/007f8b0c.md)
- [0082b53c](../0082b/0082b53c.md)
- [008a209c](../008a2/008a209c.md)
- [008e0bc0](../008e0/008e0bc0.md)
- [008e68f8](../008e6/008e68f8.md)
- [0094d124](../0094d/0094d124.md)
- [0094f7d0](../0094f/0094f7d0.md)
- [00957f9c](../00957/00957f9c.md)
- [00963004](../00963/00963004.md)
- [009a9670](../009a9/009a9670.md)
- [009a9774](../009a9/009a9774.md)
- [00a02c30](../00a02/00a02c30.md)
- [00a11cc0](../00a11/00a11cc0.md)
- [00a15464](../00a15/00a15464.md)
- [00a17ce0](../00a17/00a17ce0.md)
- [00a1bb38](../00a1b/00a1bb38.md)
- [00a1fc08](../00a1f/00a1fc08.md)
- [00a5c348](../00a5c/00a5c348.md)
- [00a5c504](../00a5c/00a5c504.md)
- [00a601cc](../00a60/00a601cc.md)
- [00a61490](../00a61/00a61490.md)
- [00aa8e8c](../00aa8/00aa8e8c.md)
- [00ade2f4](../00ade/00ade2f4.md)
- [00adf8e0](../00adf/00adf8e0.md)

## 呼び出し先

- [00419064](../00419/00419064.md)
- [0081f580](../0081f/0081f580.md)
- [00bdaff0](../00bda/00bdaff0.md)

## 疑似コード / UTF-8 3794 bytes

~~~c

undefined1 FUN_00ade5cc(undefined8 param_1,int param_2)

{
  undefined1 uVar1;
  long lVar2;
  long lVar3;
  undefined8 *puVar4;
  undefined8 *puVar5;
  long *plVar6;
  long lVar7;
  undefined8 *puVar8;
  undefined8 *puVar9;
  
  lVar2 = FUN_0081f580();
  lVar7 = *(long *)(lVar2 + 0x22a0);
  lVar2 = lVar2 + 0x22a0;
  lVar3 = lVar2;
  if (lVar7 != 0) {
    do {
      if (param_2 <= *(int *)(lVar7 + 0x1c)) {
        lVar3 = lVar7;
      }
      lVar7 = *(long *)(lVar7 + (ulong)(*(int *)(lVar7 + 0x1c) < param_2) * 8);
    } while (lVar7 != 0);
    if ((lVar3 != lVar2) && (*(int *)(lVar3 + 0x1c) <= param_2)) {
      lVar2 = lVar3;
    }
  }
  lVar3 = FUN_0081f580();
  if (lVar2 == lVar3 + 0x22a0) {
                    /* catch() { ... } // from try @ 00ade0c0 with catch @ 00ade6e0 */
    uVar1 = 0;
  }
  else {
    lVar2 = FUN_0081f580();
    puVar5 = *(undefined8 **)(lVar2 + 0x22a0);
    if (*(undefined8 **)(lVar2 + 0x22a0) == (undefined8 *)0x0) {
      puVar8 = (undefined8 *)(lVar2 + 0x22a0);
      puVar9 = (undefined8 *)(lVar2 + 0x22a0);
    }
    else {
      do {
        while (puVar4 = puVar5, puVar8 = puVar4, param_2 < *(int *)((long)puVar4 + 0x1c)) {
                    /* try { // try from 00ade664 to 00bde683 has its CatchHandler @ 00ade6d4 */
          puVar5 = (undefined8 *)*puVar4;
          puVar9 = puVar4;
          if ((undefined8 *)*puVar4 == (undefined8 *)0x0) goto LAB_00ade688;
        }
        if (param_2 <= *(int *)((long)puVar4 + 0x1c)) goto LAB_00ade6d8;
        puVar5 = (undefined8 *)puVar4[1];
      } while ((undefined8 *)puVar4[1] != (undefined8 *)0x0);
                    /* catch() { ... } // from try @ 00ade580 with catch @ 00ade684
                       try { // try from 00ade684 to 00bde74b has its CatchHandler @ 00addf84 */
      puVar9 = puVar4 + 1;
    }
LAB_00ade688:
                    /* catch() { ... } // from try @ 00ade1bc with catch @ 00ade688 */
                    /* catch() { ... } // from try @ 00ade1a8 with catch @ 00ade68c */
                    /* catch() { ... } // from try @ 00ade174 with catch @ 00ade690 */
    puVar4 = (undefined8 *)_Znwm(0x28);
                    /* catch() { ... } // from try @ 00ade090 with catch @ 00ade694
                       catch() { ... } // from try @ 00ade16c with catch @ 00ade694 */
    *puVar4 = 0;
    puVar4[1] = 0;
                    /* catch() { ... } // from try @ 00ade044 with catch @ 00ade698 */
    puVar4[2] = puVar8;
    *puVar9 = puVar4;
    plVar6 = *(long **)(lVar2 + 0x2298);
    *(int *)((long)puVar4 + 0x1c) = param_2;
                    /* catch() { ... } // from try @ 00ade02c with catch @ 00ade6b0 */
    *(undefined1 *)(puVar4 + 4) = 0;
    puVar5 = puVar4;
    if (*plVar6 != 0) {
      *(long *)(lVar2 + 0x2298) = *plVar6;
      puVar5 = (undefined8 *)*puVar9;
    }
    FUN_00419064(*(undefined8 *)(lVar2 + 0x22a0),puVar5);
                    /* catch() { ... } // from try @ 00addff4 with catch @ 00ade6cc */
                    /* catch() { ... } // from try @ 00ade664 with catch @ 00ade6d4 */
    *(long *)(lVar2 + 0x22a8) = *(long *)(lVar2 + 0x22a8) + 1;
LAB_00ade6d8:
                    /* catch() { ... } // from try @ 00ade248 with catch @ 00ade6d8 */
    uVar1 = *(undefined1 *)(puVar4 + 4);
  }
                    /* catch() { ... } // from try @ 00ade410 with catch @ 00ade6e4 */
                    /* catch() { ... } // from try @ 00ade0b4 with catch @ 00ade6e8 */
                    /* catch() { ... } // from try @ 00ade41c with catch @ 00ade6ec
                       catch() { ... } // from try @ 00ade4ec with catch @ 00ade6ec */
                    /* catch() { ... } // from try @ 00ade0cc with catch @ 00ade6f0 */
                    /* catch() { ... } // from try @ 00ade42c with catch @ 00ade6f4 */
  return uVar1;
}

~~~
