# 00afdb3c

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00afdb3c.md)

## 関数情報

~~~json
{
  "address": "00afdb3c",
  "name": "firebase::Path::PopFrontDirectory",
  "size": 248,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "5281001cbb248189e4ea7fb4947ee971466cfb96bc0671b82005fcc1a06d9dfd",
  "source_text_sha256": "5281001cbb248189e4ea7fb4947ee971466cfb96bc0671b82005fcc1a06d9dfd"
}
~~~
## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00afd1a0](../00afd/00afd1a0.md)
- [00bdaf60](../00bda/00bdaf60.md)
- [00bdaf90](../00bda/00bdaf90.md)
- [00bdec30](../00bde/00bdec30.md)
- [00bdec40](../00bde/00bdec40.md)

## 疑似コード 1/1 / UTF-8 1850 bytes

~~~c

/* firebase::Path::PopFrontDirectory() const */

void firebase::Path::PopFrontDirectory(void)

{
  byte bVar1;
  long lVar2;
  byte *pbVar3;
  byte *pbVar4;
  byte *in_x0;
  basic_string *extraout_x1;
  undefined8 *in_x8;
  byte *local_68;
  byte *local_60;
  Path local_50 [16];
  void *local_40;
  long local_38;
  
                    /* try { // try from 00afdb40 to 00bfdb5b has its CatchHandler @ 00afecd4 */
  lVar2 = tpidr_el0;
  local_38 = *(long *)(lVar2 + 0x28);
                    /* try { // try from 00afdb60 to 00bfdb6f has its CatchHandler @ 00b0037c */
  if ((*in_x0 & 1) == 0) {
    if (*in_x0 >> 1 == 0) {
LAB_00afdbec:
      *in_x8 = 0;
      in_x8[1] = 0;
      in_x8[2] = 0;
      goto LAB_00afdc0c;
    }
  }
  else if (*(long *)(in_x0 + 8) == 0) goto LAB_00afdbec;
  GetDirectories();
  FUN_00afd1a0(local_50,local_68 + 0x18,local_60);
  NormalizeSlashes(local_50,extraout_x1);
  if (((byte)local_50[0] & 1) != 0) {
    operator_delete(local_40);
  }
  if (local_68 != (byte *)0x0) {
                    /* try { // try from 00afdbb0 to 00bfdbbb has its CatchHandler @ 00afecd0 */
    if (local_60 != local_68) {
      bVar1 = local_60[-0x18];
      pbVar4 = local_60 + -0x18;
      while( true ) {
        pbVar3 = pbVar4;
                    /* try { // try from 00afdbc0 to 00bfdbdb has its CatchHandler @ 00afeccc */
        if ((bVar1 & 1) != 0) {
          operator_delete(*(void **)(local_60 + -8));
        }
        if (local_68 == pbVar3) break;
        bVar1 = pbVar3[-0x18];
        pbVar4 = pbVar3 + -0x18;
        local_60 = pbVar3;
      }
    }
    operator_delete(local_68);
  }
LAB_00afdc0c:
  if (*(long *)(lVar2 + 0x28) == local_38) {
    return;
  }
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~
