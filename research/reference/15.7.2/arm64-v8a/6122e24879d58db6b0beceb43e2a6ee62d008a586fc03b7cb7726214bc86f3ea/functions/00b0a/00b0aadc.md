# 00b0aadc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00b0aadc.md)

## 関数情報

~~~json
{
  "address": "00b0aadc",
  "name": "flatbuffers::IDLOptions::IDLOptions",
  "size": 412,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "72f759ec79363846a573a21b11993ca92b12d61dab893bf5e36ed9bf4fca4f93",
  "source_text_sha256": "72f759ec79363846a573a21b11993ca92b12d61dab893bf5e36ed9bf4fca4f93"
}
~~~
## 呼び出し元

- [00bde900](../00bde/00bde900.md)

## 呼び出し先

- [00bdaf40](../00bda/00bdaf40.md)
- [00bde1c0](../00bde/00bde1c0.md)
- [00bde630](../00bde/00bde630.md)

## 疑似コード 1/1 / UTF-8 5906 bytes

~~~c

/* flatbuffers::IDLOptions::IDLOptions(flatbuffers::IDLOptions const&) */

void __thiscall flatbuffers::IDLOptions::IDLOptions(IDLOptions *this,IDLOptions *param_1)

{
  basic_string *pbVar1;
  basic_string *pbVar2;
  undefined4 uVar3;
  IDLOptions IVar4;
  undefined2 uVar5;
  ulong uVar6;
  basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>> *this_00;
  undefined8 uVar7;
  undefined8 uVar8;
  undefined8 uVar9;
  
  uVar7 = *(undefined8 *)(param_1 + 9);
  uVar9 = *(undefined8 *)(param_1 + 8);
  uVar8 = *(undefined8 *)param_1;
  *(undefined8 *)(this + 0x11) = *(undefined8 *)(param_1 + 0x11);
  *(undefined8 *)(this + 9) = uVar7;
  *(undefined8 *)(this + 8) = uVar9;
  *(undefined8 *)this = uVar8;
  std::__ndk1::basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>>::
  basic_string((basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>> *)
               (this + 0x20),(basic_string *)(param_1 + 0x20));
  std::__ndk1::basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>>::
  basic_string((basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>> *)
               (this + 0x38),(basic_string *)(param_1 + 0x38));
  *(undefined4 *)(this + 0x50) = *(undefined4 *)(param_1 + 0x50);
  std::__ndk1::basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>>::
  basic_string((basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>> *)
               (this + 0x58),(basic_string *)(param_1 + 0x58));
  std::__ndk1::basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>>::
  basic_string((basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>> *)
               (this + 0x70),(basic_string *)(param_1 + 0x70));
  uVar5 = *(undefined2 *)(param_1 + 0x88);
  this[0x8a] = param_1[0x8a];
  *(undefined2 *)(this + 0x88) = uVar5;
  std::__ndk1::basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>>::
  basic_string((basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>> *)
               (this + 0x90),(basic_string *)(param_1 + 0x90));
  uVar3 = *(undefined4 *)(param_1 + 0xa8);
  this[0xac] = param_1[0xac];
  *(undefined4 *)(this + 0xa8) = uVar3;
  std::__ndk1::basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>>::
  basic_string((basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>> *)
               (this + 0xb0),(basic_string *)(param_1 + 0xb0));
  std::__ndk1::basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>>::
  basic_string((basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>> *)
               (this + 200),(basic_string *)(param_1 + 200));
  *(undefined4 *)(this + 0xe0) = *(undefined4 *)(param_1 + 0xe0);
  std::__ndk1::basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>>::
  basic_string((basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>> *)
               (this + 0xe8),(basic_string *)(param_1 + 0xe8));
  uVar5 = *(undefined2 *)(param_1 + 0x100);
  IVar4 = param_1[0x102];
  *(undefined8 *)(this + 0x110) = 0;
  *(undefined8 *)(this + 0x118) = 0;
  *(undefined8 *)(this + 0x108) = 0;
  *(undefined2 *)(this + 0x100) = uVar5;
  this[0x102] = IVar4;
  uVar6 = *(long *)(param_1 + 0x110) - *(long *)(param_1 + 0x108);
  if (uVar6 != 0) {
    if (0xaaaaaaaaaaaaaaa < (ulong)(((long)uVar6 >> 3) * -0x5555555555555555)) {
                    /* WARNING: Subroutine does not return */
      abort();
    }
    this_00 = operator_new(uVar6);
    *(basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>> **)
     (this + 0x108) = this_00;
    *(basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>> **)
     (this + 0x110) = this_00;
    *(basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>> **)
     (this + 0x118) = this_00 + ((long)uVar6 >> 3) * 8;
    pbVar2 = *(basic_string **)(param_1 + 0x110);
    for (pbVar1 = *(basic_string **)(param_1 + 0x108); pbVar1 != pbVar2; pbVar1 = pbVar1 + 0x18) {
      std::__ndk1::basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>>::
      basic_string(this_00,pbVar1);
      this_00 = this_00 + 0x18;
    }
    *(basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>> **)
     (this + 0x110) = this_00;
  }
  std::__ndk1::basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>>::
  basic_string((basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>> *)
               (this + 0x120),(basic_string *)(param_1 + 0x120));
  std::__ndk1::basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>>::
  basic_string((basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>> *)
               (this + 0x138),(basic_string *)(param_1 + 0x138));
  std::__ndk1::basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>>::
  basic_string((basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>> *)
               (this + 0x150),(basic_string *)(param_1 + 0x150));
  std::__ndk1::basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>>::
  basic_string((basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>> *)
               (this + 0x168),(basic_string *)(param_1 + 0x168));
  uVar8 = *(undefined8 *)(param_1 + 0x188);
  uVar7 = *(undefined8 *)(param_1 + 0x180);
  *(undefined2 *)(this + 400) = *(undefined2 *)(param_1 + 400);
  *(undefined8 *)(this + 0x188) = uVar8;
  *(undefined8 *)(this + 0x180) = uVar7;
  return;
}

~~~
