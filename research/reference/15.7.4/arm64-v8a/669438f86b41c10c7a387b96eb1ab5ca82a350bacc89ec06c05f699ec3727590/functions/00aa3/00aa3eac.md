# 00aa3eac

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00aa3e68`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa3/00aa3e68.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/priority-0058.md#compare-8bf93f5520a7c4add3b3b4f8a1f76d55)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 要確認
  - [v15.7.4 → v16.0.0 候補と検査根拠](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/review-0089.md#review-27f01f0e2f8d8c04c8474296e4fe316d)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aa3eac",
  "name": "FUN_00aa3eac",
  "size": 184,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "1c60eee775d5eb6009b41de0d017127ef26351cb76ed0d263c706facf26605bd",
  "source_text_sha256": "1c60eee775d5eb6009b41de0d017127ef26351cb76ed0d263c706facf26605bd",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00aa3eac",
        "00aa3f63"
      ]
    ],
    "bytes_sha256": "4398a540deee06be51b0b95e3ae244025c186c70f0c88d4ae6789501bae7478f",
    "instruction_count": 46,
    "instruction_bytes": 184,
    "body_bytes": 184,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [006a0ab4](../006a0/006a0ab4.md)
- [009f1ea8](../009f1/009f1ea8.md)
- [00aa0f64](../00aa0/00aa0f64.md)

## 呼び出し先

- [005c2710](../005c2/005c2710.md)
- [0081f580](../0081f/0081f580.md)
- [00aa2c70](../00aa2/00aa2c70.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 570 bytes

~~~c

ulong FUN_00aa3eac(int param_1,int param_2,int param_3)

{
  long lVar1;
  ulong uVar2;
  
  lVar1 = FUN_0081f580();
  uVar2 = FUN_005c2710(lVar1 + (long)param_1 * 0x1f0 + 0x2678);
  lVar1 = FUN_0081f580();
  if ((uVar2 & 1) == 0) {
    uVar2 = (ulong)(*(int *)((long)__DT_JMPREL + lVar1 + ((long)param_2 + 2) * 0x1c4 + 0xa50c) != 0)
    ;
  }
  else {
    if (*(int *)(lVar1 + ((long)param_2 + 2) * 0x770 + (long)param_3 * 0x1dc + 0x9f03c) == 0) {
      uVar2 = FUN_00aa2c70(lVar1,param_2,param_3,0x44);
      return uVar2;
    }
    uVar2 = 1;
  }
  return uVar2;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00aa3eac"></a> `00aa3eac` | `fd 7b bd a9` | stp x29,x30,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00aa3eb0"></a> `00aa3eb0` | `f5 0b 00 f9` | str x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aa3eb4"></a> `00aa3eb4` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00aa3eb8"></a> `00aa3eb8` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00aa3ebc"></a> `00aa3ebc` | `f3 03 02 2a` | mov w19,w2 | `FALL_THROUGH`
<a id="insn-00aa3ec0"></a> `00aa3ec0` | `f4 03 01 2a` | mov w20,w1 | `FALL_THROUGH`
<a id="insn-00aa3ec4"></a> `00aa3ec4` | `f5 03 00 2a` | mov w21,w0 | `FALL_THROUGH`
<a id="insn-00aa3ec8"></a> `00aa3ec8` | `ae ed f5 97` | bl 0x0081f580 | `UNCONDITIONAL_CALL`
<a id="insn-00aa3ecc"></a> `00aa3ecc` | `08 3e 80 52` | mov w8,#0x1f0 | `FALL_THROUGH`
<a id="insn-00aa3ed0"></a> `00aa3ed0` | `09 cf 84 52` | mov w9,#0x2678 | `FALL_THROUGH`
<a id="insn-00aa3ed4"></a> `00aa3ed4` | `a8 02 28 9b` | smaddl x8,w21,w8,x0 | `FALL_THROUGH`
<a id="insn-00aa3ed8"></a> `00aa3ed8` | `00 01 09 8b` | add x0,x8,x9 | `FALL_THROUGH`
<a id="insn-00aa3edc"></a> `00aa3edc` | `0d 7a ec 97` | bl 0x005c2710 | `UNCONDITIONAL_CALL`
<a id="insn-00aa3ee0"></a> `00aa3ee0` | `f5 03 00 2a` | mov w21,w0 | `FALL_THROUGH`
<a id="insn-00aa3ee4"></a> `00aa3ee4` | `a7 ed f5 97` | bl 0x0081f580 | `UNCONDITIONAL_CALL`
<a id="insn-00aa3ee8"></a> `00aa3ee8` | `88 7e 40 93` | sxtw x8,w20 | `FALL_THROUGH`
<a id="insn-00aa3eec"></a> `00aa3eec` | `08 09 00 91` | add x8,x8,#0x2 | `FALL_THROUGH`
<a id="insn-00aa3ef0"></a> `00aa3ef0` | `35 01 00 37` | tbnz w21,#0x0,0x00aa3f14 | `CONDITIONAL_JUMP`
<a id="insn-00aa3ef4"></a> `00aa3ef4` | `89 38 80 52` | mov w9,#0x1c4 | `FALL_THROUGH`
<a id="insn-00aa3ef8"></a> `00aa3ef8` | `08 01 09 9b` | madd x8,x8,x9,x0 | `FALL_THROUGH`
<a id="insn-00aa3efc"></a> `00aa3efc` | `89 e8 93 52` | mov w9,#0x9f44 | `FALL_THROUGH`
<a id="insn-00aa3f00"></a> `00aa3f00` | `69 04 a0 72` | movk w9,#0x23, LSL #16 | `FALL_THROUGH`
<a id="insn-00aa3f04"></a> `00aa3f04` | `08 69 69 b8` | ldr w8,[x8, x9, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00aa3f08"></a> `00aa3f08` | `1f 01 00 71` | cmp w8,#0x0 | `FALL_THROUGH`
<a id="insn-00aa3f0c"></a> `00aa3f0c` | `e0 07 9f 1a` | cset w0,ne | `FALL_THROUGH`
<a id="insn-00aa3f10"></a> `00aa3f10` | `0a 00 00 14` | b 0x00aa3f38 | `UNCONDITIONAL_JUMP`
<a id="insn-00aa3f14"></a> `00aa3f14` | `09 ee 80 52` | mov w9,#0x770 | `FALL_THROUGH`
<a id="insn-00aa3f18"></a> `00aa3f18` | `08 01 09 9b` | madd x8,x8,x9,x0 | `FALL_THROUGH`
<a id="insn-00aa3f1c"></a> `00aa3f1c` | `89 3b 80 52` | mov w9,#0x1dc | `FALL_THROUGH`
<a id="insn-00aa3f20"></a> `00aa3f20` | `68 22 29 9b` | smaddl x8,w19,w9,x8 | `FALL_THROUGH`
<a id="insn-00aa3f24"></a> `00aa3f24` | `89 07 9e 52` | mov w9,#0xf03c | `FALL_THROUGH`
<a id="insn-00aa3f28"></a> `00aa3f28` | `29 01 a0 72` | movk w9,#0x9, LSL #16 | `FALL_THROUGH`
<a id="insn-00aa3f2c"></a> `00aa3f2c` | `08 69 69 b8` | ldr w8,[x8, x9, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00aa3f30"></a> `00aa3f30` | `c8 00 00 34` | cbz w8,0x00aa3f48 | `CONDITIONAL_JUMP`
<a id="insn-00aa3f34"></a> `00aa3f34` | `20 00 80 52` | mov w0,#0x1 | `FALL_THROUGH`
<a id="insn-00aa3f38"></a> `00aa3f38` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00aa3f3c"></a> `00aa3f3c` | `f5 0b 40 f9` | ldr x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aa3f40"></a> `00aa3f40` | `fd 7b c3 a8` | ldp x29,x30,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00aa3f44"></a> `00aa3f44` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00aa3f48"></a> `00aa3f48` | `e1 03 14 2a` | mov w1,w20 | `FALL_THROUGH`
<a id="insn-00aa3f4c"></a> `00aa3f4c` | `e2 03 13 2a` | mov w2,w19 | `FALL_THROUGH`
<a id="insn-00aa3f50"></a> `00aa3f50` | `83 08 80 52` | mov w3,#0x44 | `FALL_THROUGH`
<a id="insn-00aa3f54"></a> `00aa3f54` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00aa3f58"></a> `00aa3f58` | `f5 0b 40 f9` | ldr x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aa3f5c"></a> `00aa3f5c` | `fd 7b c3 a8` | ldp x29,x30,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00aa3f60"></a> `00aa3f60` | `44 fb ff 17` | b 0x00aa2c70 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00aa3eac`](#insn-00aa3eac) 範囲 `[['00aa3eac', '00aa3ef3']]`
  - `CONDITIONAL_JUMP` [`00aa3ef0`](#insn-00aa3ef0) → [`00aa3f14`](#insn-00aa3f14)
  - `FALL_THROUGH` [`00aa3ef0`](#insn-00aa3ef0) → [`00aa3ef4`](#insn-00aa3ef4)
- ブロック [`00aa3ef4`](#insn-00aa3ef4) 範囲 `[['00aa3ef4', '00aa3f13']]`
  - `UNCONDITIONAL_JUMP` [`00aa3f10`](#insn-00aa3f10) → [`00aa3f38`](#insn-00aa3f38)
- ブロック [`00aa3f14`](#insn-00aa3f14) 範囲 `[['00aa3f14', '00aa3f33']]`
  - `CONDITIONAL_JUMP` [`00aa3f30`](#insn-00aa3f30) → [`00aa3f48`](#insn-00aa3f48)
  - `FALL_THROUGH` [`00aa3f30`](#insn-00aa3f30) → [`00aa3f34`](#insn-00aa3f34)
- ブロック [`00aa3f34`](#insn-00aa3f34) 範囲 `[['00aa3f34', '00aa3f37']]`
  - `FALL_THROUGH` [`00aa3f34`](#insn-00aa3f34) → [`00aa3f38`](#insn-00aa3f38)
- ブロック [`00aa3f38`](#insn-00aa3f38) 範囲 `[['00aa3f38', '00aa3f47']]`
- ブロック [`00aa3f48`](#insn-00aa3f48) 範囲 `[['00aa3f48', '00aa3f63']]`

## 命令位置別の参照

- [`00aa3eac`](#insn-00aa3eac) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa3eb0`](#insn-00aa3eb0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa3eb4`](#insn-00aa3eb4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa3ec8`](#insn-00aa3ec8) → [`0081f580`](../0081f/0081f580.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0081f580` · 推定シンボル `None` · 推定型 `None`
- [`00aa3edc`](#insn-00aa3edc) → [`005c2710`](../005c2/005c2710.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `005c2710` · 推定シンボル `None` · 推定型 `None`
- [`00aa3ee4`](#insn-00aa3ee4) → [`0081f580`](../0081f/0081f580.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0081f580` · 推定シンボル `None` · 推定型 `None`
- [`00aa3ef0`](#insn-00aa3ef0) → [`00aa3f14`](#insn-00aa3f14) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa3f04`](#insn-00aa3f04) → `00239f44`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `Elf64_Rela[1792]`
- [`00aa3f10`](#insn-00aa3f10) → [`00aa3f38`](#insn-00aa3f38) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa3f30`](#insn-00aa3f30) → [`00aa3f48`](#insn-00aa3f48) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa3f38`](#insn-00aa3f38) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa3f3c`](#insn-00aa3f3c) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa3f40`](#insn-00aa3f40) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa3f54`](#insn-00aa3f54) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa3f58`](#insn-00aa3f58) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa3f5c`](#insn-00aa3f5c) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa3f60`](#insn-00aa3f60) → [`00aa2c70`](../00aa2/00aa2c70.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00aa2c70` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00aa3eac`](#insn-00aa3eac)

~~~json
{
  "source": "00aa3eac",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa3eb0`](#insn-00aa3eb0)

~~~json
{
  "source": "00aa3eb0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa3eb4`](#insn-00aa3eb4)

~~~json
{
  "source": "00aa3eb4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa3ec8`](#insn-00aa3ec8)

~~~json
{
  "source": "00aa3ec8",
  "target": "0081f580",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aa3edc`](#insn-00aa3edc)

~~~json
{
  "source": "00aa3edc",
  "target": "005c2710",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aa3ee4`](#insn-00aa3ee4)

~~~json
{
  "source": "00aa3ee4",
  "target": "0081f580",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aa3ef0`](#insn-00aa3ef0)

~~~json
{
  "source": "00aa3ef0",
  "target": "00aa3f14",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa3f04`](#insn-00aa3f04)

~~~json
{
  "source": "00aa3f04",
  "target": "00239f44",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0022fa38",
  "offset": 42252,
  "size": 43008,
  "datatype": "Elf64_Rela[1792]",
  "bytes": "a0c0b1000000000002040000010000000000000000000000a8c0b10000000000",
  "capture_start": "0022fa38",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00aa3f10`](#insn-00aa3f10)

~~~json
{
  "source": "00aa3f10",
  "target": "00aa3f38",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa3f30`](#insn-00aa3f30)

~~~json
{
  "source": "00aa3f30",
  "target": "00aa3f48",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa3f38`](#insn-00aa3f38)

~~~json
{
  "source": "00aa3f38",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa3f3c`](#insn-00aa3f3c)

~~~json
{
  "source": "00aa3f3c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa3f40`](#insn-00aa3f40)

~~~json
{
  "source": "00aa3f40",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa3f54`](#insn-00aa3f54)

~~~json
{
  "source": "00aa3f54",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa3f58`](#insn-00aa3f58)

~~~json
{
  "source": "00aa3f58",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa3f5c`](#insn-00aa3f5c)

~~~json
{
  "source": "00aa3f5c",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa3f60`](#insn-00aa3f60)

~~~json
{
  "source": "00aa3f60",
  "target": "00aa2c70",
  "target_space": "ram",
  "resolution": "function"
}
~~~
