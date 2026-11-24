# 00b4bcfc

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00b4bc60`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4bc60.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0073.md#compare-646dfe0f15d9090606102fd580b8f8f9)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `00b4ccf0`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4c/00b4ccf0.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0075.md#compare-8e089d479589f327b5ad0ce1a99f4172)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00b4bcfc",
  "name": "_ZN8firebase4util8iterable13CacheFieldIdsEP7_JNIEnvP8_jobject",
  "size": 112,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "e9d032bef7f4a68d47f5a9ceacc523940cb9faea2e9fd06e552aedbd286221a4",
  "source_text_sha256": "e9d032bef7f4a68d47f5a9ceacc523940cb9faea2e9fd06e552aedbd286221a4",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00b4bcfc",
        "00b4bd6b"
      ]
    ],
    "bytes_sha256": "3d8e21f2fa598aef653d7359619c2916fd0a2d73682c4d4559646bdb2bd065d9",
    "instruction_count": 28,
    "instruction_bytes": 112,
    "body_bytes": 112,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c5afc0](../00c5a/00c5afc0.md)
- [00c5afe0](../00c5a/00c5afe0.md)

## 関連文字列（未確認候補）

~~~text
"java/lang/Iterable"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 594 bytes

~~~c

void _ZN8firebase4util8iterable13CacheFieldIdsEP7_JNIEnvP8_jobject
               (undefined8 param_1,undefined8 param_2)

{
  if (DAT_01125c98 == 0) {
    DAT_01125c98 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             (param_1,param_2,0,"java/lang/Iterable",0);
  }
  _ZN8firebase4util14LookupFieldIdsEP7_JNIEnvP7_jclassPKNS0_15FieldDescriptorEmPP9_jfieldIDPKc
            (param_1,DAT_01125c98,&DAT_0030b900,1,&DAT_01125cb0,"java/lang/Iterable");
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00b4bcfc"></a> `00b4bcfc` | `f4 4f be a9` | stp x20,x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00b4bd00"></a> `00b4bd00` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b4bd04"></a> `00b4bd04` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00b4bd08"></a> `00b4bd08` | `d4 2e 00 d0` | adrp x20,0x1125000 | `FALL_THROUGH`
<a id="insn-00b4bd0c"></a> `00b4bd0c` | `e8 03 01 aa` | mov x8,x1 | `FALL_THROUGH`
<a id="insn-00b4bd10"></a> `00b4bd10` | `81 4e 46 f9` | ldr x1,[x20, #0xc98] | `FALL_THROUGH`
<a id="insn-00b4bd14"></a> `00b4bd14` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00b4bd18"></a> `00b4bd18` | `41 01 00 b5` | cbnz x1,0x00b4bd40 | `CONDITIONAL_JUMP`
<a id="insn-00b4bd1c"></a> `00b4bd1c` | `a3 ba ff 90` | adrp x3,0x29f000 | `FALL_THROUGH`
<a id="insn-00b4bd20"></a> `00b4bd20` | `63 a4 24 91` | add x3,x3,#0x929 | `FALL_THROUGH`
<a id="insn-00b4bd24"></a> `00b4bd24` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00b4bd28"></a> `00b4bd28` | `e1 03 08 aa` | mov x1,x8 | `FALL_THROUGH`
<a id="insn-00b4bd2c"></a> `00b4bd2c` | `e2 03 1f aa` | mov x2,xzr | `FALL_THROUGH`
<a id="insn-00b4bd30"></a> `00b4bd30` | `e4 03 1f 2a` | mov w4,wzr | `FALL_THROUGH`
<a id="insn-00b4bd34"></a> `00b4bd34` | `ab 3c 04 94` | bl 0x00c5afe0 | `UNCONDITIONAL_CALL`
<a id="insn-00b4bd38"></a> `00b4bd38` | `e1 03 00 aa` | mov x1,x0 | `FALL_THROUGH`
<a id="insn-00b4bd3c"></a> `00b4bd3c` | `80 4e 06 f9` | str x0,[x20, #0xc98] | `FALL_THROUGH`
<a id="insn-00b4bd40"></a> `00b4bd40` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b4bd44"></a> `00b4bd44` | `02 be ff 90` | adrp x2,0x30b000 | `FALL_THROUGH`
<a id="insn-00b4bd48"></a> `00b4bd48` | `c4 2e 00 d0` | adrp x4,0x1125000 | `FALL_THROUGH`
<a id="insn-00b4bd4c"></a> `00b4bd4c` | `a5 ba ff 90` | adrp x5,0x29f000 | `FALL_THROUGH`
<a id="insn-00b4bd50"></a> `00b4bd50` | `42 00 24 91` | add x2,x2,#0x900 | `FALL_THROUGH`
<a id="insn-00b4bd54"></a> `00b4bd54` | `84 c0 32 91` | add x4,x4,#0xcb0 | `FALL_THROUGH`
<a id="insn-00b4bd58"></a> `00b4bd58` | `a5 a4 24 91` | add x5,x5,#0x929 | `FALL_THROUGH`
<a id="insn-00b4bd5c"></a> `00b4bd5c` | `23 00 80 52` | mov w3,#0x1 | `FALL_THROUGH`
<a id="insn-00b4bd60"></a> `00b4bd60` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00b4bd64"></a> `00b4bd64` | `f4 4f c2 a8` | ldp x20,x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00b4bd68"></a> `00b4bd68` | `96 3c 04 14` | b 0x00c5afc0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00b4bcfc`](#insn-00b4bcfc) 範囲 `[['00b4bcfc', '00b4bd1b']]`
  - `CONDITIONAL_JUMP` [`00b4bd18`](#insn-00b4bd18) → [`00b4bd40`](#insn-00b4bd40)
  - `FALL_THROUGH` [`00b4bd18`](#insn-00b4bd18) → [`00b4bd1c`](#insn-00b4bd1c)
- ブロック [`00b4bd1c`](#insn-00b4bd1c) 範囲 `[['00b4bd1c', '00b4bd3f']]`
  - `FALL_THROUGH` [`00b4bd3c`](#insn-00b4bd3c) → [`00b4bd40`](#insn-00b4bd40)
- ブロック [`00b4bd40`](#insn-00b4bd40) 範囲 `[['00b4bd40', '00b4bd6b']]`

## 命令位置別の参照

- [`00b4bcfc`](#insn-00b4bcfc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4bd00`](#insn-00b4bd00) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4bd10`](#insn-00b4bd10) → `01125c98`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00b4bd18`](#insn-00b4bd18) → [`00b4bd40`](#insn-00b4bd40) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4bd20`](#insn-00b4bd20) → `0029f929`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00b4bd34`](#insn-00b4bd34) → [`00c5afe0`](../00c5a/00c5afe0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5afe0` · 推定シンボル `None` · 推定型 `None`
- [`00b4bd3c`](#insn-00b4bd3c) → `01125c98`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00b4bd40`](#insn-00b4bd40) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4bd50`](#insn-00b4bd50) → `0030b900`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4bd54`](#insn-00b4bd54) → `01125cb0`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4bd58`](#insn-00b4bd58) → `0029f929`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00b4bd68`](#insn-00b4bd68) → [`00c5afc0`](../00c5a/00c5afc0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5afc0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00b4bcfc`](#insn-00b4bcfc)

~~~json
{
  "source": "00b4bcfc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4bd00`](#insn-00b4bd00)

~~~json
{
  "source": "00b4bd00",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4bd10`](#insn-00b4bd10)

~~~json
{
  "source": "00b4bd10",
  "target": "01125c98",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01125c98",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00b4bd18`](#insn-00b4bd18)

~~~json
{
  "source": "00b4bd18",
  "target": "00b4bd40",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4bd20`](#insn-00b4bd20)

~~~json
{
  "source": "00b4bd20",
  "target": "0029f929",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0029f929",
  "offset": 0,
  "size": 19,
  "datatype": "string",
  "bytes": "6a6176612f6c616e672f4974657261626c6500",
  "capture_start": "0029f929",
  "capture_bytes": 19,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00b4bd34`](#insn-00b4bd34)

~~~json
{
  "source": "00b4bd34",
  "target": "00c5afe0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b4bd3c`](#insn-00b4bd3c)

~~~json
{
  "source": "00b4bd3c",
  "target": "01125c98",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01125c98",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00b4bd40`](#insn-00b4bd40)

~~~json
{
  "source": "00b4bd40",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4bd50`](#insn-00b4bd50)

~~~json
{
  "source": "00b4bd50",
  "target": "0030b900",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4bd54`](#insn-00b4bd54)

~~~json
{
  "source": "00b4bd54",
  "target": "01125cb0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4bd58`](#insn-00b4bd58)

~~~json
{
  "source": "00b4bd58",
  "target": "0029f929",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0029f929",
  "offset": 0,
  "size": 19,
  "datatype": "string",
  "bytes": "6a6176612f6c616e672f4974657261626c6500",
  "capture_start": "0029f929",
  "capture_bytes": 19,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00b4bd68`](#insn-00b4bd68)

~~~json
{
  "source": "00b4bd68",
  "target": "00c5afc0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
