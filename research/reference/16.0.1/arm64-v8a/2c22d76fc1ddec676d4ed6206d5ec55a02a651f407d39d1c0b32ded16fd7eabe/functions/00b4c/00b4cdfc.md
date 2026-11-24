# 00b4cdfc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00b4c9d4`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4c/00b4c9d4.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0073.md#compare-c046aa050c4b803d36af50adfd98bcac)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00b4ce98`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4c/00b4ce98.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0073.md#compare-f5fa6d12cd4efd41397031040e9178bb)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00b4cdfc",
  "name": "_ZN8firebase4util22parcel_file_descriptor14CacheMethodIdsEP7_JNIEnvP8_jobject",
  "size": 112,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "29ba4fbabe3baa85ea3ae80a40c646324b7a909cb793e366d0b22775652b6b14",
  "source_text_sha256": "29ba4fbabe3baa85ea3ae80a40c646324b7a909cb793e366d0b22775652b6b14",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00b4cdfc",
        "00b4ce6b"
      ]
    ],
    "bytes_sha256": "859ca182acecee0aa916de796833310a7fe377d63c015918568b56f49865f965",
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

- [00c5af10](../00c5a/00c5af10.md)
- [00c5af30](../00c5a/00c5af30.md)

## 関連文字列（未確認候補）

~~~text
"android/os/ParcelFileDescriptor"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 668 bytes

~~~c

void _ZN8firebase4util22parcel_file_descriptor14CacheMethodIdsEP7_JNIEnvP8_jobject
               (undefined8 param_1,undefined8 param_2)

{
  if (DAT_01125c68 == 0) {
    DAT_01125c68 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             (param_1,param_2,0,"android/os/ParcelFileDescriptor",0);
  }
  _ZN8firebase4util15LookupMethodIdsEP7_JNIEnvP7_jclassPKNS0_19MethodNameSignatureEmPP10_jmethodIDPKc
            (param_1,DAT_01125c68,&PTR_s_detachFd_00c900a0,1,&DAT_01125c78,
             "android/os/ParcelFileDescriptor");
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00b4cdfc"></a> `00b4cdfc` | `f4 4f be a9` | stp x20,x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00b4ce00"></a> `00b4ce00` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b4ce04"></a> `00b4ce04` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00b4ce08"></a> `00b4ce08` | `d4 2e 00 b0` | adrp x20,0x1125000 | `FALL_THROUGH`
<a id="insn-00b4ce0c"></a> `00b4ce0c` | `e8 03 01 aa` | mov x8,x1 | `FALL_THROUGH`
<a id="insn-00b4ce10"></a> `00b4ce10` | `81 36 46 f9` | ldr x1,[x20, #0xc68] | `FALL_THROUGH`
<a id="insn-00b4ce14"></a> `00b4ce14` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00b4ce18"></a> `00b4ce18` | `41 01 00 b5` | cbnz x1,0x00b4ce40 | `CONDITIONAL_JUMP`
<a id="insn-00b4ce1c"></a> `00b4ce1c` | `a3 ba ff f0` | adrp x3,0x2a3000 | `FALL_THROUGH`
<a id="insn-00b4ce20"></a> `00b4ce20` | `63 bc 2c 91` | add x3,x3,#0xb2f | `FALL_THROUGH`
<a id="insn-00b4ce24"></a> `00b4ce24` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00b4ce28"></a> `00b4ce28` | `e1 03 08 aa` | mov x1,x8 | `FALL_THROUGH`
<a id="insn-00b4ce2c"></a> `00b4ce2c` | `e2 03 1f aa` | mov x2,xzr | `FALL_THROUGH`
<a id="insn-00b4ce30"></a> `00b4ce30` | `e4 03 1f 2a` | mov w4,wzr | `FALL_THROUGH`
<a id="insn-00b4ce34"></a> `00b4ce34` | `37 38 04 94` | bl 0x00c5af10 | `UNCONDITIONAL_CALL`
<a id="insn-00b4ce38"></a> `00b4ce38` | `e1 03 00 aa` | mov x1,x0 | `FALL_THROUGH`
<a id="insn-00b4ce3c"></a> `00b4ce3c` | `80 36 06 f9` | str x0,[x20, #0xc68] | `FALL_THROUGH`
<a id="insn-00b4ce40"></a> `00b4ce40` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b4ce44"></a> `00b4ce44` | `22 0a 00 90` | adrp x2,0xc90000 | `FALL_THROUGH`
<a id="insn-00b4ce48"></a> `00b4ce48` | `c4 2e 00 b0` | adrp x4,0x1125000 | `FALL_THROUGH`
<a id="insn-00b4ce4c"></a> `00b4ce4c` | `a5 ba ff f0` | adrp x5,0x2a3000 | `FALL_THROUGH`
<a id="insn-00b4ce50"></a> `00b4ce50` | `42 80 02 91` | add x2,x2,#0xa0 | `FALL_THROUGH`
<a id="insn-00b4ce54"></a> `00b4ce54` | `84 e0 31 91` | add x4,x4,#0xc78 | `FALL_THROUGH`
<a id="insn-00b4ce58"></a> `00b4ce58` | `a5 bc 2c 91` | add x5,x5,#0xb2f | `FALL_THROUGH`
<a id="insn-00b4ce5c"></a> `00b4ce5c` | `23 00 80 52` | mov w3,#0x1 | `FALL_THROUGH`
<a id="insn-00b4ce60"></a> `00b4ce60` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00b4ce64"></a> `00b4ce64` | `f4 4f c2 a8` | ldp x20,x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00b4ce68"></a> `00b4ce68` | `32 38 04 14` | b 0x00c5af30 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00b4cdfc`](#insn-00b4cdfc) 範囲 `[['00b4cdfc', '00b4ce1b']]`
  - `CONDITIONAL_JUMP` [`00b4ce18`](#insn-00b4ce18) → [`00b4ce40`](#insn-00b4ce40)
  - `FALL_THROUGH` [`00b4ce18`](#insn-00b4ce18) → [`00b4ce1c`](#insn-00b4ce1c)
- ブロック [`00b4ce1c`](#insn-00b4ce1c) 範囲 `[['00b4ce1c', '00b4ce3f']]`
  - `FALL_THROUGH` [`00b4ce3c`](#insn-00b4ce3c) → [`00b4ce40`](#insn-00b4ce40)
- ブロック [`00b4ce40`](#insn-00b4ce40) 範囲 `[['00b4ce40', '00b4ce6b']]`

## 命令位置別の参照

- [`00b4cdfc`](#insn-00b4cdfc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4ce00`](#insn-00b4ce00) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4ce10`](#insn-00b4ce10) → `01125c68`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00b4ce18`](#insn-00b4ce18) → [`00b4ce40`](#insn-00b4ce40) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4ce20`](#insn-00b4ce20) → `002a3b2f`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00b4ce34`](#insn-00b4ce34) → [`00c5af10`](../00c5a/00c5af10.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5af10` · 推定シンボル `None` · 推定型 `None`
- [`00b4ce3c`](#insn-00b4ce3c) → `01125c68`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00b4ce40`](#insn-00b4ce40) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4ce50`](#insn-00b4ce50) → `00c900a0`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00b4ce54`](#insn-00b4ce54) → `01125c78`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4ce58`](#insn-00b4ce58) → `002a3b2f`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00b4ce68`](#insn-00b4ce68) → [`00c5af30`](../00c5a/00c5af30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5af30` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00b4cdfc`](#insn-00b4cdfc)

~~~json
{
  "source": "00b4cdfc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4ce00`](#insn-00b4ce00)

~~~json
{
  "source": "00b4ce00",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4ce10`](#insn-00b4ce10)

~~~json
{
  "source": "00b4ce10",
  "target": "01125c68",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01125c68",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00b4ce18`](#insn-00b4ce18)

~~~json
{
  "source": "00b4ce18",
  "target": "00b4ce40",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4ce20`](#insn-00b4ce20)

~~~json
{
  "source": "00b4ce20",
  "target": "002a3b2f",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a3b2f",
  "offset": 0,
  "size": 32,
  "datatype": "string",
  "bytes": "616e64726f69642f6f732f50617263656c46696c6544657363726970746f7200",
  "capture_start": "002a3b2f",
  "capture_bytes": 32,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00b4ce34`](#insn-00b4ce34)

~~~json
{
  "source": "00b4ce34",
  "target": "00c5af10",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b4ce3c`](#insn-00b4ce3c)

~~~json
{
  "source": "00b4ce3c",
  "target": "01125c68",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01125c68",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00b4ce40`](#insn-00b4ce40)

~~~json
{
  "source": "00b4ce40",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4ce50`](#insn-00b4ce50)

~~~json
{
  "source": "00b4ce50",
  "target": "00c900a0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c900a0",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00b4ce54`](#insn-00b4ce54)

~~~json
{
  "source": "00b4ce54",
  "target": "01125c78",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4ce58`](#insn-00b4ce58)

~~~json
{
  "source": "00b4ce58",
  "target": "002a3b2f",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a3b2f",
  "offset": 0,
  "size": 32,
  "datatype": "string",
  "bytes": "616e64726f69642f6f732f50617263656c46696c6544657363726970746f7200",
  "capture_start": "002a3b2f",
  "capture_bytes": 32,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00b4ce68`](#insn-00b4ce68)

~~~json
{
  "source": "00b4ce68",
  "target": "00c5af30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
