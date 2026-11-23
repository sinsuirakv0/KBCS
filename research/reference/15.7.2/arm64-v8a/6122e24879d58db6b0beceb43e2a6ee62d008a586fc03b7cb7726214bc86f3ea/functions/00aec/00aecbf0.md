# 00aecbf0

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00aeccb8`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aeccb8.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0061.md#compare-7e5cc80c4527c8adf6bf612f9b6e5f31)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aecbf0",
  "name": "_ZN8firebase4util22parcel_file_descriptor13CacheFieldIdsEP7_JNIEnvP8_jobject",
  "size": 112,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "2a8d6c18995fbc6850ffa1fecead8c587fd0217b2ef9e24301ba43a054a19f5f",
  "source_text_sha256": "2a8d6c18995fbc6850ffa1fecead8c587fd0217b2ef9e24301ba43a054a19f5f",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00aecbf0",
        "00aecc5f"
      ]
    ],
    "bytes_sha256": "1d64664140d307581ab2abb29174c1f69e2570a9c274ad5ada3a97d578ded63c",
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

- [00bddf70](../00bdd/00bddf70.md)
- [00bddf90](../00bdd/00bddf90.md)

## 関連文字列（未確認候補）

~~~text
"android/os/ParcelFileDescriptor"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 635 bytes

~~~c

void _ZN8firebase4util22parcel_file_descriptor13CacheFieldIdsEP7_JNIEnvP8_jobject
               (undefined8 param_1,undefined8 param_2)

{
  if (DAT_010a08a8 == 0) {
    DAT_010a08a8 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             (param_1,param_2,0,"android/os/ParcelFileDescriptor",0);
  }
  _ZN8firebase4util14LookupFieldIdsEP7_JNIEnvP7_jclassPKNS0_15FieldDescriptorEmPP9_jfieldIDPKc
            (param_1,DAT_010a08a8,&DAT_002f5d88,1,&DAT_010a08c0,"android/os/ParcelFileDescriptor");
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00aecbf0"></a> `00aecbf0` | `f4 4f be a9` | stp x20,x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00aecbf4"></a> `00aecbf4` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aecbf8"></a> `00aecbf8` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00aecbfc"></a> `00aecbfc` | `b4 2d 00 90` | adrp x20,0x10a0000 | `FALL_THROUGH`
<a id="insn-00aecc00"></a> `00aecc00` | `e8 03 01 aa` | mov x8,x1 | `FALL_THROUGH`
<a id="insn-00aecc04"></a> `00aecc04` | `81 56 44 f9` | ldr x1,[x20, #0x8a8] | `FALL_THROUGH`
<a id="insn-00aecc08"></a> `00aecc08` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00aecc0c"></a> `00aecc0c` | `41 01 00 b5` | cbnz x1,0x00aecc34 | `CONDITIONAL_JUMP`
<a id="insn-00aecc10"></a> `00aecc10` | `43 bd ff 90` | adrp x3,0x294000 | `FALL_THROUGH`
<a id="insn-00aecc14"></a> `00aecc14` | `63 4c 07 91` | add x3,x3,#0x1d3 | `FALL_THROUGH`
<a id="insn-00aecc18"></a> `00aecc18` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aecc1c"></a> `00aecc1c` | `e1 03 08 aa` | mov x1,x8 | `FALL_THROUGH`
<a id="insn-00aecc20"></a> `00aecc20` | `e2 03 1f aa` | mov x2,xzr | `FALL_THROUGH`
<a id="insn-00aecc24"></a> `00aecc24` | `e4 03 1f 2a` | mov w4,wzr | `FALL_THROUGH`
<a id="insn-00aecc28"></a> `00aecc28` | `da c4 03 94` | bl 0x00bddf90 | `UNCONDITIONAL_CALL`
<a id="insn-00aecc2c"></a> `00aecc2c` | `e1 03 00 aa` | mov x1,x0 | `FALL_THROUGH`
<a id="insn-00aecc30"></a> `00aecc30` | `80 56 04 f9` | str x0,[x20, #0x8a8] | `FALL_THROUGH`
<a id="insn-00aecc34"></a> `00aecc34` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aecc38"></a> `00aecc38` | `42 c0 ff b0` | adrp x2,0x2f5000 | `FALL_THROUGH`
<a id="insn-00aecc3c"></a> `00aecc3c` | `a4 2d 00 90` | adrp x4,0x10a0000 | `FALL_THROUGH`
<a id="insn-00aecc40"></a> `00aecc40` | `45 bd ff 90` | adrp x5,0x294000 | `FALL_THROUGH`
<a id="insn-00aecc44"></a> `00aecc44` | `42 20 36 91` | add x2,x2,#0xd88 | `FALL_THROUGH`
<a id="insn-00aecc48"></a> `00aecc48` | `84 00 23 91` | add x4,x4,#0x8c0 | `FALL_THROUGH`
<a id="insn-00aecc4c"></a> `00aecc4c` | `a5 4c 07 91` | add x5,x5,#0x1d3 | `FALL_THROUGH`
<a id="insn-00aecc50"></a> `00aecc50` | `23 00 80 52` | mov w3,#0x1 | `FALL_THROUGH`
<a id="insn-00aecc54"></a> `00aecc54` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aecc58"></a> `00aecc58` | `f4 4f c2 a8` | ldp x20,x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00aecc5c"></a> `00aecc5c` | `c5 c4 03 14` | b 0x00bddf70 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00aecbf0`](#insn-00aecbf0) 範囲 `[['00aecbf0', '00aecc0f']]`
  - `CONDITIONAL_JUMP` [`00aecc0c`](#insn-00aecc0c) → [`00aecc34`](#insn-00aecc34)
  - `FALL_THROUGH` [`00aecc0c`](#insn-00aecc0c) → [`00aecc10`](#insn-00aecc10)
- ブロック [`00aecc10`](#insn-00aecc10) 範囲 `[['00aecc10', '00aecc33']]`
  - `FALL_THROUGH` [`00aecc30`](#insn-00aecc30) → [`00aecc34`](#insn-00aecc34)
- ブロック [`00aecc34`](#insn-00aecc34) 範囲 `[['00aecc34', '00aecc5f']]`

## 命令位置別の参照

- [`00aecbf0`](#insn-00aecbf0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aecbf4`](#insn-00aecbf4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aecc04`](#insn-00aecc04) → `010a08a8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aecc0c`](#insn-00aecc0c) → [`00aecc34`](#insn-00aecc34) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aecc14`](#insn-00aecc14) → `002941d3`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00aecc28`](#insn-00aecc28) → [`00bddf90`](../00bdd/00bddf90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bddf90` · 推定シンボル `None` · 推定型 `None`
- [`00aecc30`](#insn-00aecc30) → `010a08a8`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aecc34`](#insn-00aecc34) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aecc44`](#insn-00aecc44) → `002f5d88`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aecc48`](#insn-00aecc48) → `010a08c0`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aecc4c`](#insn-00aecc4c) → `002941d3`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00aecc5c`](#insn-00aecc5c) → [`00bddf70`](../00bdd/00bddf70.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bddf70` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00aecbf0`](#insn-00aecbf0)

~~~json
{
  "source": "00aecbf0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aecbf4`](#insn-00aecbf4)

~~~json
{
  "source": "00aecbf4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aecc04`](#insn-00aecc04)

~~~json
{
  "source": "00aecc04",
  "target": "010a08a8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a08a8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aecc0c`](#insn-00aecc0c)

~~~json
{
  "source": "00aecc0c",
  "target": "00aecc34",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aecc14`](#insn-00aecc14)

~~~json
{
  "source": "00aecc14",
  "target": "002941d3",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002941d3",
  "offset": 0,
  "size": 32,
  "datatype": "string",
  "bytes": "616e64726f69642f6f732f50617263656c46696c6544657363726970746f7200",
  "capture_start": "002941d3",
  "capture_bytes": 32,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aecc28`](#insn-00aecc28)

~~~json
{
  "source": "00aecc28",
  "target": "00bddf90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aecc30`](#insn-00aecc30)

~~~json
{
  "source": "00aecc30",
  "target": "010a08a8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a08a8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aecc34`](#insn-00aecc34)

~~~json
{
  "source": "00aecc34",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aecc44`](#insn-00aecc44)

~~~json
{
  "source": "00aecc44",
  "target": "002f5d88",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aecc48`](#insn-00aecc48)

~~~json
{
  "source": "00aecc48",
  "target": "010a08c0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aecc4c`](#insn-00aecc4c)

~~~json
{
  "source": "00aecc4c",
  "target": "002941d3",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002941d3",
  "offset": 0,
  "size": 32,
  "datatype": "string",
  "bytes": "616e64726f69642f6f732f50617263656c46696c6544657363726970746f7200",
  "capture_start": "002941d3",
  "capture_bytes": 32,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aecc5c`](#insn-00aecc5c)

~~~json
{
  "source": "00aecc5c",
  "target": "00bddf70",
  "target_space": "ram",
  "resolution": "function"
}
~~~
