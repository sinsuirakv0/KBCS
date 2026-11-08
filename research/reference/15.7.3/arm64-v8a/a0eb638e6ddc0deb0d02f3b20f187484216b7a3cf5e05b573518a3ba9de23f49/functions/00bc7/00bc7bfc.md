# 00bc7bfc

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

## 関数情報

~~~json
{
  "address": "00bc7bfc",
  "name": "FUN_00bc7bfc",
  "size": 812,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "931fb9854a63b451a7f5235ada1e0547e7db53d93126d53544f0d57a019334a2",
  "source_text_sha256": "931fb9854a63b451a7f5235ada1e0547e7db53d93126d53544f0d57a019334a2"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bdb160](../00bdb/00bdb160.md)
- [00bdd200](../00bdd/00bdd200.md)
- [00bde270](../00bde/00bde270.md)

## 疑似コード / UTF-8 6994 bytes

~~~c

void FUN_00bc7bfc(long param_1,undefined8 *param_2)

{
  void *pvVar1;
  size_t __size;
  long lVar2;
  long lVar3;
  ulong uVar4;
  long *plVar5;
  size_t sVar6;
  void *__src;
  
  plVar5 = *(long **)(param_1 + 0x10);
  if ((uint)((int)((uint)*(ushort *)((long)plVar5 + 9) << 0x1a) >> 0x1a) <
      ((int)((uint)*(ushort *)(param_1 + 9) << 0x1a) >> 0x1a) + 1U) {
    (**(code **)(*plVar5 + 0x20))(plVar5,param_2);
    if ((*(ushort *)((long)plVar5 + 9) & 0xc0) != 0x40) {
      (**(code **)(*plVar5 + 0x28))(plVar5,param_2);
    }
    sVar6 = *(size_t *)(param_1 + 0x20);
  }
  else {
    lVar2 = param_2[1];
    pvVar1 = (void *)*param_2;
    uVar4 = lVar2 + 1;
    *(int *)(param_2 + 4) = *(int *)(param_2 + 4) + 1;
    if ((ulong)param_2[2] < uVar4) {
      sVar6 = param_2[2] * 2;
      uVar4 = lVar2 + 0x3e1;
      if (sVar6 < uVar4 || sVar6 - uVar4 == 0) {
        sVar6 = uVar4;
      }
      param_2[2] = sVar6;
      pvVar1 = realloc(pvVar1,sVar6);
      *param_2 = pvVar1;
      if (pvVar1 == (void *)0x0) {
                    /* WARNING: Subroutine does not return */
        abort();
      }
      lVar2 = param_2[1];
      uVar4 = lVar2 + 1;
    }
    param_2[1] = uVar4;
    lVar3 = *plVar5;
    *(undefined1 *)((long)pvVar1 + lVar2) = 0x28;
                    /* try { // try from 00bc7cdc to 00cc7ce3 has its CatchHandler @ 00bc8d4c */
    (**(code **)(lVar3 + 0x20))(plVar5,param_2);
    if ((*(ushort *)((long)plVar5 + 9) & 0xc0) != 0x40) {
                    /* try { // try from 00bc7cf8 to 00cc7cff has its CatchHandler @ 00bc8d44 */
      (**(code **)(*plVar5 + 0x28))(plVar5,param_2);
    }
    lVar2 = param_2[1];
    pvVar1 = (void *)*param_2;
                    /* try { // try from 00bc7d14 to 00cc7d1b has its CatchHandler @ 00bc8d48 */
    uVar4 = lVar2 + 1;
    *(int *)(param_2 + 4) = *(int *)(param_2 + 4) + -1;
    if ((ulong)param_2[2] < uVar4) {
      sVar6 = param_2[2] * 2;
      uVar4 = lVar2 + 0x3e1;
                    /* try { // try from 00bc7d30 to 00cc7d37 has its CatchHandler @ 00bc8d40 */
      if (sVar6 < uVar4 || sVar6 - uVar4 == 0) {
        sVar6 = uVar4;
      }
      param_2[2] = sVar6;
      pvVar1 = realloc(pvVar1,sVar6);
      *param_2 = pvVar1;
      if (pvVar1 == (void *)0x0) {
                    /* WARNING: Subroutine does not return */
        abort();
      }
      lVar2 = param_2[1];
                    /* try { // try from 00bc7d4c to 00cc7d53 has its CatchHandler @ 00bc8d3c */
      uVar4 = lVar2 + 1;
    }
    param_2[1] = uVar4;
    *(undefined1 *)((long)pvVar1 + lVar2) = 0x29;
    sVar6 = *(size_t *)(param_1 + 0x20);
  }
  if (sVar6 != 0) {
    lVar2 = param_2[1];
                    /* try { // try from 00bc7d68 to 00cc7d6f has its CatchHandler @ 00bc8d38 */
    pvVar1 = (void *)*param_2;
    __src = *(void **)(param_1 + 0x18);
    if ((ulong)param_2[2] < lVar2 + sVar6) {
      __size = param_2[2] * 2;
      uVar4 = lVar2 + sVar6 + 0x3e0;
                    /* try { // try from 00bc7d84 to 00cc7d87 has its CatchHandler @ 00bc8d48 */
      if (__size < uVar4 || __size - uVar4 == 0) {
        __size = uVar4;
      }
      param_2[2] = __size;
      pvVar1 = realloc(pvVar1,__size);
      *param_2 = pvVar1;
      if (pvVar1 == (void *)0x0) {
                    /* WARNING: Subroutine does not return */
                    /* try { // try from 00bc7f14 to 00cc7f1b has its CatchHandler @ 00bc8c28 */
        abort();
      }
                    /* try { // try from 00bc7d9c to 00cc7d9f has its CatchHandler @ 00bc8d4c */
      lVar2 = param_2[1];
    }
    memcpy((void *)((long)pvVar1 + lVar2),__src,sVar6);
                    /* try { // try from 00bc7db4 to 00cc7db7 has its CatchHandler @ 00bc8d44 */
    param_2[1] = param_2[1] + sVar6;
  }
  plVar5 = *(long **)(param_1 + 0x28);
                    /* try { // try from 00bc7dcc to 00cc7dcf has its CatchHandler @ 00bc8d40 */
  if ((*(ushort *)((long)plVar5 + 9) & 0x3f) < (*(ushort *)(param_1 + 9) & 0x3f)) {
                    /* try { // try from 00bc7de4 to 00cc7de7 has its CatchHandler @ 00bc8d38 */
    (**(code **)(*plVar5 + 0x20))(plVar5,param_2);
    if ((*(ushort *)((long)plVar5 + 9) & 0xc0) != 0x40) {
                    /* try { // try from 00bc7dfc to 00cc7dff has its CatchHandler @ 00bc8d3c */
                    /* try { // try from 00bc7e14 to 00cc7e17 has its CatchHandler @ 00bc8c94 */
                    /* WARNING: Could not recover jumptable at 0x00bc7e1c. Too many branches */
                    /* WARNING: Treating indirect jump as call */
      (**(code **)(*plVar5 + 0x28))(plVar5,param_2);
      return;
    }
  }
  else {
    lVar2 = param_2[1];
    pvVar1 = (void *)*param_2;
                    /* try { // try from 00bc7e2c to 00cc7e33 has its CatchHandler @ 00bc8c7c */
    uVar4 = lVar2 + 1;
    *(int *)(param_2 + 4) = *(int *)(param_2 + 4) + 1;
    if ((ulong)param_2[2] < uVar4) {
      sVar6 = param_2[2] * 2;
      uVar4 = lVar2 + 0x3e1;
                    /* try { // try from 00bc7e48 to 00cc7e4f has its CatchHandler @ 00bc8c78 */
      if (sVar6 < uVar4 || sVar6 - uVar4 == 0) {
        sVar6 = uVar4;
      }
      param_2[2] = sVar6;
      pvVar1 = realloc(pvVar1,sVar6);
      *param_2 = pvVar1;
      if (pvVar1 == (void *)0x0) {
                    /* WARNING: Subroutine does not return */
        abort();
      }
      lVar2 = param_2[1];
                    /* try { // try from 00bc7e64 to 00cc7e6b has its CatchHandler @ 00bc8c74 */
      uVar4 = lVar2 + 1;
    }
    param_2[1] = uVar4;
    lVar3 = *plVar5;
    *(undefined1 *)((long)pvVar1 + lVar2) = 0x28;
                    /* try { // try from 00bc7e80 to 00cc7e87 has its CatchHandler @ 00bc8c70 */
    (**(code **)(lVar3 + 0x20))(plVar5,param_2);
    if ((*(ushort *)((long)plVar5 + 9) & 0xc0) != 0x40) {
                    /* try { // try from 00bc7e9c to 00cc7e9f has its CatchHandler @ 00bc8c94 */
      (**(code **)(*plVar5 + 0x28))(plVar5,param_2);
    }
    lVar2 = param_2[1];
                    /* try { // try from 00bc7eb4 to 00cc7eb7 has its CatchHandler @ 00bc8c7c */
    pvVar1 = (void *)*param_2;
    uVar4 = lVar2 + 1;
    *(int *)(param_2 + 4) = *(int *)(param_2 + 4) + -1;
    if ((ulong)param_2[2] < uVar4) {
                    /* try { // try from 00bc7ecc to 00cc7ecf has its CatchHandler @ 00bc8c78 */
      sVar6 = param_2[2] * 2;
      uVar4 = lVar2 + 0x3e1;
      if (sVar6 < uVar4 || sVar6 - uVar4 == 0) {
        sVar6 = uVar4;
      }
      param_2[2] = sVar6;
      pvVar1 = realloc(pvVar1,sVar6);
                    /* try { // try from 00bc7ee4 to 00cc7ee7 has its CatchHandler @ 00bc8c74 */
      *param_2 = pvVar1;
      if (pvVar1 == (void *)0x0) {
                    /* WARNING: Subroutine does not return */
        abort();
      }
      lVar2 = param_2[1];
      uVar4 = lVar2 + 1;
    }
    param_2[1] = uVar4;
                    /* try { // try from 00bc7efc to 00cc7eff has its CatchHandler @ 00bc8c70 */
    *(undefined1 *)((long)pvVar1 + lVar2) = 0x29;
  }
  return;
}

~~~
