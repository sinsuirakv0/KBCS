# 00aa1dac

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

## 関数情報

~~~json
{
  "address": "00aa1dac",
  "name": "FUN_00aa1dac",
  "size": 284,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "db4c0530df0aaa57ff60b47b497ad4c19f700847a92c8969a36e63006012dcec",
  "source_text_sha256": "db4c0530df0aaa57ff60b47b497ad4c19f700847a92c8969a36e63006012dcec"
}
~~~

## 呼び出し元

- [00aa0268](../00aa0/00aa0268.md)

## 呼び出し先

- [0043bba4](../0043b/0043bba4.md)
- [00aa1aa0](../00aa1/00aa1aa0.md)
- [00aa1c48](../00aa1/00aa1c48.md)
- [00c57ee0](../00c57/00c57ee0.md)

## 疑似コード / UTF-8 1757 bytes

~~~c

void FUN_00aa1dac(long *param_1,long *param_2,long *param_3)

{
  long lVar1;
  bool bVar2;
  long *plVar3;
  undefined8 *puVar4;
  undefined1 auStack_70 [8];
  undefined8 local_68;
  undefined8 *apuStack_60 [3];
  long local_48;
  
  lVar1 = tpidr_el0;
  local_48 = *(long *)(lVar1 + 0x28);
  do {
    while( true ) {
      if (param_2 == param_3) {
        if (*(long *)(lVar1 + 0x28) != local_48) {
                    /* WARNING: Subroutine does not return */
          __stack_chk_fail();
        }
        return;
      }
      plVar3 = (long *)FUN_00aa1aa0(param_1,param_1 + 1,&local_68,auStack_70,param_2 + 4);
      if (*plVar3 != 0) break;
      FUN_00aa1c48(apuStack_60,param_1,param_2 + 4);
                    /* try { // try from 00aa1e38 to 00ba1e3b has its CatchHandler @ 00aa2a90 */
      *apuStack_60[0] = 0;
      apuStack_60[0][1] = 0;
                    /* try { // try from 00aa1e3c to 00ba1f63 has its CatchHandler @ 00aa1600 */
      apuStack_60[0][2] = local_68;
      *plVar3 = (long)apuStack_60[0];
      puVar4 = apuStack_60[0];
      if (*(long *)*param_1 != 0) {
        *param_1 = *(long *)*param_1;
        puVar4 = (undefined8 *)*plVar3;
      }
      FUN_0043bba4(param_1[1],puVar4);
      param_1[2] = param_1[2] + 1;
      plVar3 = (long *)param_2[1];
      if ((long *)param_2[1] == (long *)0x0) goto LAB_00aa1e84;
LAB_00aa1e74:
      do {
        param_2 = plVar3;
        plVar3 = (long *)*param_2;
      } while ((long *)*param_2 != (long *)0x0);
    }
    plVar3 = (long *)param_2[1];
    if ((long *)param_2[1] != (long *)0x0) goto LAB_00aa1e74;
LAB_00aa1e84:
    do {
      plVar3 = (long *)param_2[2];
      bVar2 = (long *)*plVar3 != param_2;
      param_2 = plVar3;
    } while (bVar2);
  } while( true );
}

~~~
