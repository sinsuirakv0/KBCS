# 004cadbc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](004cadbc.md)

## 関数情報

~~~json
{
  "address": "004cadbc",
  "name": "Botan::PKCS8::load_key",
  "size": 244,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "c5bf8b079a8c2fd71bc744364299a723a15f88cc1c2526ca7dbb5be7cab10298",
  "source_text_sha256": "c5bf8b079a8c2fd71bc744364299a723a15f88cc1c2526ca7dbb5be7cab10298"
}
~~~
## 呼び出し元

- [00bdc6e0](../00bdc/00bdc6e0.md)

## 呼び出し先

- [00418fe0](../00418/00418fe0.md)
- [004c9e38](../004c9/004c9e38.md)
- [005229d4](../00522/005229d4.md)
- [00bdaf40](../00bda/00bdaf40.md)
- [00bdaf60](../00bda/00bdaf60.md)
- [00bdaf90](../00bda/00bdaf90.md)

## 疑似コード 1/1 / UTF-8 1357 bytes

~~~c

/* Botan::PKCS8::load_key(Botan::DataSource&, std::__ndk1::basic_string<char,
   std::__ndk1::char_traits<char>, std::__ndk1::allocator<char> > const&) */

void __thiscall Botan::PKCS8::load_key(PKCS8 *this,DataSource *param_1,basic_string *param_2)

{
  long lVar1;
  long *plVar2;
  ulong local_90;
  long lStack_88;
  void *local_80;
  undefined1 auStack_70 [32];
  long *local_50;
  long local_38;
  
  lVar1 = tpidr_el0;
  local_38 = *(long *)(lVar1 + 0x28);
  if (((byte)*param_1 & 1) == 0) {
    lStack_88 = *(long *)(param_1 + 8);
    local_90 = *(ulong *)param_1;
    local_80 = *(void **)(param_1 + 0x10);
  }
  else {
    FUN_00418fe0(&local_90,*(undefined8 *)(param_1 + 0x10),*(undefined8 *)(param_1 + 8));
  }
  local_50 = (long *)0x0;
  plVar2 = operator_new(0x20);
  *plVar2 = (long)&PTR_FUN_00bed460;
  if ((local_90 & 1) == 0) {
    plVar2[2] = lStack_88;
    plVar2[1] = local_90;
    plVar2[3] = (long)local_80;
  }
  else {
    FUN_00418fe0(plVar2 + 1,local_80,lStack_88);
  }
  local_50 = plVar2;
  FUN_004c9e38(this,auStack_70,1);
  (**(code **)(*plVar2 + 0x28))(plVar2);
  if ((local_90 & 1) != 0) {
    operator_delete(local_80);
  }
  if (*(long *)(lVar1 + 0x28) == local_38) {
    return;
  }
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~
