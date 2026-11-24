# 00bdeb1c

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bddb28`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bddb28.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0085.md#compare-eaad0acaa75d330f2e35467696910217)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdeb1c",
  "name": "_ZN8firebase4auth8metadata13CacheFieldIdsEP7_JNIEnvP8_jobject",
  "size": 112,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "c7fdb1802297d41cb868f53b9cd30983154231f43abf96c5b1a7b2b461a8cb1e",
  "source_text_sha256": "c7fdb1802297d41cb868f53b9cd30983154231f43abf96c5b1a7b2b461a8cb1e",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdeb1c",
        "00bdeb8b"
      ]
    ],
    "bytes_sha256": "8d79782938f1724881927a5377ae315c61a7c4d4686d3d238678ddc5d5ed9e1e",
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

- [00c5bf90](../00c5b/00c5bf90.md)
- [00c5bfb0](../00c5b/00c5bfb0.md)

## 関連文字列（未確認候補）

~~~text
"%PG%com/google/firebase/auth/FirebaseUserMetadata"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 662 bytes

~~~c

void _ZN8firebase4auth8metadata13CacheFieldIdsEP7_JNIEnvP8_jobject
               (undefined8 param_1,undefined8 param_2)

{
  if (DAT_01127ec0 == 0) {
    DAT_01127ec0 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             (param_1,param_2,0,"com/google/firebase/auth/FirebaseUserMetadata",0);
  }
  _ZN8firebase4util14LookupFieldIdsEP7_JNIEnvP7_jclassPKNS0_15FieldDescriptorEmPP9_jfieldIDPKc
            (param_1,DAT_01127ec0,&DAT_00310298,1,&DAT_01127ee0,
             "com/google/firebase/auth/FirebaseUserMetadata");
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdeb1c"></a> `00bdeb1c` | `f4 4f be a9` | stp x20,x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00bdeb20"></a> `00bdeb20` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bdeb24"></a> `00bdeb24` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bdeb28"></a> `00bdeb28` | `54 2a 00 b0` | adrp x20,0x1127000 | `FALL_THROUGH`
<a id="insn-00bdeb2c"></a> `00bdeb2c` | `e8 03 01 aa` | mov x8,x1 | `FALL_THROUGH`
<a id="insn-00bdeb30"></a> `00bdeb30` | `81 62 47 f9` | ldr x1,[x20, #0xec0] | `FALL_THROUGH`
<a id="insn-00bdeb34"></a> `00bdeb34` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bdeb38"></a> `00bdeb38` | `41 01 00 b5` | cbnz x1,0x00bdeb60 | `CONDITIONAL_JUMP`
<a id="insn-00bdeb3c"></a> `00bdeb3c` | `03 b7 ff 90` | adrp x3,0x2be000 | `FALL_THROUGH`
<a id="insn-00bdeb40"></a> `00bdeb40` | `63 dc 28 91` | add x3,x3,#0xa37 | `FALL_THROUGH`
<a id="insn-00bdeb44"></a> `00bdeb44` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bdeb48"></a> `00bdeb48` | `e1 03 08 aa` | mov x1,x8 | `FALL_THROUGH`
<a id="insn-00bdeb4c"></a> `00bdeb4c` | `e2 03 1f aa` | mov x2,xzr | `FALL_THROUGH`
<a id="insn-00bdeb50"></a> `00bdeb50` | `e4 03 1f 2a` | mov w4,wzr | `FALL_THROUGH`
<a id="insn-00bdeb54"></a> `00bdeb54` | `17 f5 01 94` | bl 0x00c5bfb0 | `UNCONDITIONAL_CALL`
<a id="insn-00bdeb58"></a> `00bdeb58` | `e1 03 00 aa` | mov x1,x0 | `FALL_THROUGH`
<a id="insn-00bdeb5c"></a> `00bdeb5c` | `80 62 07 f9` | str x0,[x20, #0xec0] | `FALL_THROUGH`
<a id="insn-00bdeb60"></a> `00bdeb60` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bdeb64"></a> `00bdeb64` | `82 b9 ff d0` | adrp x2,0x310000 | `FALL_THROUGH`
<a id="insn-00bdeb68"></a> `00bdeb68` | `44 2a 00 b0` | adrp x4,0x1127000 | `FALL_THROUGH`
<a id="insn-00bdeb6c"></a> `00bdeb6c` | `05 b7 ff 90` | adrp x5,0x2be000 | `FALL_THROUGH`
<a id="insn-00bdeb70"></a> `00bdeb70` | `42 60 0a 91` | add x2,x2,#0x298 | `FALL_THROUGH`
<a id="insn-00bdeb74"></a> `00bdeb74` | `84 80 3b 91` | add x4,x4,#0xee0 | `FALL_THROUGH`
<a id="insn-00bdeb78"></a> `00bdeb78` | `a5 dc 28 91` | add x5,x5,#0xa37 | `FALL_THROUGH`
<a id="insn-00bdeb7c"></a> `00bdeb7c` | `23 00 80 52` | mov w3,#0x1 | `FALL_THROUGH`
<a id="insn-00bdeb80"></a> `00bdeb80` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bdeb84"></a> `00bdeb84` | `f4 4f c2 a8` | ldp x20,x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00bdeb88"></a> `00bdeb88` | `02 f5 01 14` | b 0x00c5bf90 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdeb1c`](#insn-00bdeb1c) 範囲 `[['00bdeb1c', '00bdeb3b']]`
  - `CONDITIONAL_JUMP` [`00bdeb38`](#insn-00bdeb38) → [`00bdeb60`](#insn-00bdeb60)
  - `FALL_THROUGH` [`00bdeb38`](#insn-00bdeb38) → [`00bdeb3c`](#insn-00bdeb3c)
- ブロック [`00bdeb3c`](#insn-00bdeb3c) 範囲 `[['00bdeb3c', '00bdeb5f']]`
  - `FALL_THROUGH` [`00bdeb5c`](#insn-00bdeb5c) → [`00bdeb60`](#insn-00bdeb60)
- ブロック [`00bdeb60`](#insn-00bdeb60) 範囲 `[['00bdeb60', '00bdeb8b']]`

## 命令位置別の参照

- [`00bdeb1c`](#insn-00bdeb1c) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdeb20`](#insn-00bdeb20) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdeb30`](#insn-00bdeb30) → `01127ec0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bdeb38`](#insn-00bdeb38) → [`00bdeb60`](#insn-00bdeb60) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdeb40`](#insn-00bdeb40) → `002bea37`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bdeb54`](#insn-00bdeb54) → [`00c5bfb0`](../00c5b/00c5bfb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5bfb0` · 推定シンボル `None` · 推定型 `None`
- [`00bdeb5c`](#insn-00bdeb5c) → `01127ec0`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bdeb60`](#insn-00bdeb60) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdeb70`](#insn-00bdeb70) → `00310298`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdeb74`](#insn-00bdeb74) → `01127ee0`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdeb78`](#insn-00bdeb78) → `002bea37`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bdeb88`](#insn-00bdeb88) → [`00c5bf90`](../00c5b/00c5bf90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5bf90` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdeb1c`](#insn-00bdeb1c)

~~~json
{
  "source": "00bdeb1c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdeb20`](#insn-00bdeb20)

~~~json
{
  "source": "00bdeb20",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdeb30`](#insn-00bdeb30)

~~~json
{
  "source": "00bdeb30",
  "target": "01127ec0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127ec0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bdeb38`](#insn-00bdeb38)

~~~json
{
  "source": "00bdeb38",
  "target": "00bdeb60",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdeb40`](#insn-00bdeb40)

~~~json
{
  "source": "00bdeb40",
  "target": "002bea37",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002bea33",
  "offset": 4,
  "size": 50,
  "datatype": "string",
  "bytes": "25504725636f6d2f676f6f676c652f66697265626173652f617574682f466972",
  "capture_start": "002bea33",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00bdeb54`](#insn-00bdeb54)

~~~json
{
  "source": "00bdeb54",
  "target": "00c5bfb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdeb5c`](#insn-00bdeb5c)

~~~json
{
  "source": "00bdeb5c",
  "target": "01127ec0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127ec0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bdeb60`](#insn-00bdeb60)

~~~json
{
  "source": "00bdeb60",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdeb70`](#insn-00bdeb70)

~~~json
{
  "source": "00bdeb70",
  "target": "00310298",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdeb74`](#insn-00bdeb74)

~~~json
{
  "source": "00bdeb74",
  "target": "01127ee0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdeb78`](#insn-00bdeb78)

~~~json
{
  "source": "00bdeb78",
  "target": "002bea37",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002bea33",
  "offset": 4,
  "size": 50,
  "datatype": "string",
  "bytes": "25504725636f6d2f676f6f676c652f66697265626173652f617574682f466972",
  "capture_start": "002bea33",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00bdeb88`](#insn-00bdeb88)

~~~json
{
  "source": "00bdeb88",
  "target": "00c5bf90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
