# 00ba8ffc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00ba8ffc.md)

## 関数情報

~~~json
{
  "address": "00ba8ffc",
  "name": "std::__ndk1::collate_byname<wchar_t>::collate_byname",
  "size": 188,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "197446273832c26cc96d2659fecb89b0bbfbcfa1e8083530e6fbfd0f51e6e714",
  "source_text_sha256": "197446273832c26cc96d2659fecb89b0bbfbcfa1e8083530e6fbfd0f51e6e714"
}
~~~
## 呼び出し元

- [00be1740](../00be1/00be1740.md)

## 呼び出し先

- [00bd6fec](../00bd6/00bd6fec.md)
- [00bdaf60](../00bda/00bdaf60.md)
- [00bdb160](../00bdb/00bdb160.md)
- [00bdb3b0](../00bdb/00bdb3b0.md)
- [00be0eb0](../00be0/00be0eb0.md)
- [00be1470](../00be1/00be1470.md)

## 関連文字列（未確認候補）

~~~text
"collate_byname<wchar_t>::collate_byname(size_t refs) failed to construct for "
~~~
## 疑似コード 1/1 / UTF-8 1439 bytes

~~~c

/* std::__ndk1::collate_byname<wchar_t>::collate_byname(std::__ndk1::basic_string<char,
   std::__ndk1::char_traits<char>, std::__ndk1::allocator<char> > const&, unsigned long) */

void __thiscall
std::__ndk1::collate_byname<wchar_t>::collate_byname
          (collate_byname<wchar_t> *this,basic_string *param_1,ulong param_2)

{
  char *pcVar1;
  __locale_t p_Var2;
  undefined8 uVar3;
  basic_string *pbVar4;
  basic_string *__locale;
  byte local_38;
  char acStack_37 [15];
  char *local_28;
  
  *(undefined **)this = PTR_vtable_00c1be90 + 0x10;
  *(ulong *)(this + 8) = param_2 - 1;
  __locale = *(basic_string **)(param_1 + 0x10);
  if (((byte)*param_1 & 1) == 0) {
    __locale = param_1 + 1;
  }
  pbVar4 = (basic_string *)0x0;
  p_Var2 = newlocale(0x1fbf,(char *)__locale,(__locale_t)0x0);
  *(__locale_t *)(this + 0x10) = p_Var2;
  if (p_Var2 != (__locale_t)0x0) {
    return;
  }
  operator+((__ndk1 *)
            "collate_byname<wchar_t>::collate_byname(size_t refs) failed to construct for ",
            (char *)param_1,pbVar4);
  pcVar1 = local_28;
  if ((local_38 & 1) == 0) {
    pcVar1 = acStack_37;
  }
  uVar3 = __throw_runtime_error(pcVar1);
  if ((local_38 & 1) != 0) {
    operator_delete(local_28);
  }
  __shared_weak_count::~__shared_weak_count((__shared_weak_count *)this);
                    /* WARNING: Subroutine does not return */
  FUN_00bd6fec(uVar3);
}

~~~
