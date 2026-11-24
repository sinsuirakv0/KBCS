# 00bc8ffc

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bc8008`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc8/00bc8008.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0081.md#compare-95af459eebbb8caf9d22b81c8f1f5043)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bc8ffc",
  "name": "_ZN8firebase13remote_config8internal20RemoteConfigInternal10GetBooleanEPKcPNS0_9ValueInfoE",
  "size": 244,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "d4413db116d566fa973c02549308ac3fe8dbe72bee6b8439c3030febb10fa69d",
  "source_text_sha256": "d4413db116d566fa973c02549308ac3fe8dbe72bee6b8439c3030febb10fa69d",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bc8ffc",
        "00bc90ef"
      ]
    ],
    "bytes_sha256": "7da42577d4d8b3e038f8a312f471d89f6ff8b1eb4f6db4df2e78c7f9630d4e27",
    "instruction_count": 61,
    "instruction_bytes": 244,
    "body_bytes": 244,
    "indirect": 4,
    "unresolved": 4
  }
}
~~~

## 呼び出し元

- [00c5e760](../00c5e/00c5e760.md)

## 呼び出し先

- [00497da8](../00497/00497da8.md)
- [00bc90f0](../00bc9/00bc90f0.md)
- [00c5bd40](../00c5b/00c5bd40.md)
- [00c5c120](../00c5c/00c5c120.md)

## 関連文字列（未確認候補）

~~~text
"Remote Config: Failed to retrieve %s value from key %s"
"boolean"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 952 bytes

~~~c

bool _ZN8firebase13remote_config8internal20RemoteConfigInternal10GetBooleanEPKcPNS0_9ValueInfoE
               (undefined8 *param_1,undefined8 param_2,long param_3)

{
  bool bVar1;
  char cVar2;
  char cVar3;
  long *plVar4;
  long lVar5;
  
  plVar4 = (long *)_ZNK8firebase3App9GetJNIEnvEv(*param_1);
  lVar5 = FUN_00bc90f0(plVar4,param_1[0x33],param_2,param_3);
  bVar1 = false;
  if (lVar5 != 0) {
    cVar2 = FUN_00497da8(plVar4,lVar5,DAT_01127610);
    cVar3 = (**(code **)(*plVar4 + 0x720))(plVar4);
    bVar1 = cVar3 == '\0';
    if (!bVar1) {
      (**(code **)(*plVar4 + 0x80))(plVar4);
      (**(code **)(*plVar4 + 0x88))(plVar4);
      _ZN8firebase8LogErrorEPKcz
                ("Remote Config: Failed to retrieve %s value from key %s","boolean",param_2);
    }
    (**(code **)(*plVar4 + 0xb8))(plVar4,lVar5);
    if (param_3 != 0) {
      *(bool *)(param_3 + 4) = bVar1;
    }
    bVar1 = cVar2 != '\0' && bVar1;
  }
  return bVar1;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bc8ffc"></a> `00bc8ffc` | `f7 0f 1c f8` | str x23,[sp, #-0x40]! | `FALL_THROUGH`
<a id="insn-00bc9000"></a> `00bc9000` | `f6 57 01 a9` | stp x22,x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bc9004"></a> `00bc9004` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bc9008"></a> `00bc9008` | `fd 7b 03 a9` | stp x29,x30,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bc900c"></a> `00bc900c` | `fd c3 00 91` | add x29,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00bc9010"></a> `00bc9010` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00bc9014"></a> `00bc9014` | `00 00 40 f9` | ldr x0,[x0] | `FALL_THROUGH`
<a id="insn-00bc9018"></a> `00bc9018` | `f3 03 02 aa` | mov x19,x2 | `FALL_THROUGH`
<a id="insn-00bc901c"></a> `00bc901c` | `f6 03 01 aa` | mov x22,x1 | `FALL_THROUGH`
<a id="insn-00bc9020"></a> `00bc9020` | `40 4c 02 94` | bl 0x00c5c120 | `UNCONDITIONAL_CALL`
<a id="insn-00bc9024"></a> `00bc9024` | `81 ce 40 f9` | ldr x1,[x20, #0x198] | `FALL_THROUGH`
<a id="insn-00bc9028"></a> `00bc9028` | `e2 03 16 aa` | mov x2,x22 | `FALL_THROUGH`
<a id="insn-00bc902c"></a> `00bc902c` | `e3 03 13 aa` | mov x3,x19 | `FALL_THROUGH`
<a id="insn-00bc9030"></a> `00bc9030` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00bc9034"></a> `00bc9034` | `2f 00 00 94` | bl 0x00bc90f0 | `UNCONDITIONAL_CALL`
<a id="insn-00bc9038"></a> `00bc9038` | `20 05 00 b4` | cbz x0,0x00bc90dc | `CONDITIONAL_JUMP`
<a id="insn-00bc903c"></a> `00bc903c` | `e8 2a 00 d0` | adrp x8,0x1127000 | `FALL_THROUGH`
<a id="insn-00bc9040"></a> `00bc9040` | `02 09 43 f9` | ldr x2,[x8, #0x610] | `FALL_THROUGH`
<a id="insn-00bc9044"></a> `00bc9044` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00bc9048"></a> `00bc9048` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bc904c"></a> `00bc904c` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00bc9050"></a> `00bc9050` | `56 3b e3 97` | bl 0x00497da8 | `UNCONDITIONAL_CALL`
<a id="insn-00bc9054"></a> `00bc9054` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-00bc9058"></a> `00bc9058` | `f7 03 00 2a` | mov w23,w0 | `FALL_THROUGH`
<a id="insn-00bc905c"></a> `00bc905c` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bc9060"></a> `00bc9060` | `08 91 43 f9` | ldr x8,[x8, #0x720] | `FALL_THROUGH`
<a id="insn-00bc9064"></a> `00bc9064` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bc9068"></a> `00bc9068` | `1f 1c 00 72` | tst w0,#0xff | `FALL_THROUGH`
<a id="insn-00bc906c"></a> `00bc906c` | `20 02 00 54` | b.eq 0x00bc90b0 | `CONDITIONAL_JUMP`
<a id="insn-00bc9070"></a> `00bc9070` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-00bc9074"></a> `00bc9074` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bc9078"></a> `00bc9078` | `08 41 40 f9` | ldr x8,[x8, #0x80] | `FALL_THROUGH`
<a id="insn-00bc907c"></a> `00bc907c` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bc9080"></a> `00bc9080` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-00bc9084"></a> `00bc9084` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bc9088"></a> `00bc9088` | `08 45 40 f9` | ldr x8,[x8, #0x88] | `FALL_THROUGH`
<a id="insn-00bc908c"></a> `00bc908c` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bc9090"></a> `00bc9090` | `a0 b6 ff f0` | adrp x0,0x2a0000 | `FALL_THROUGH`
<a id="insn-00bc9094"></a> `00bc9094` | `01 b7 ff b0` | adrp x1,0x2aa000 | `FALL_THROUGH`
<a id="insn-00bc9098"></a> `00bc9098` | `00 24 33 91` | add x0,x0,#0xcc9 | `FALL_THROUGH`
<a id="insn-00bc909c"></a> `00bc909c` | `21 40 26 91` | add x1,x1,#0x990 | `FALL_THROUGH`
<a id="insn-00bc90a0"></a> `00bc90a0` | `e2 03 16 aa` | mov x2,x22 | `FALL_THROUGH`
<a id="insn-00bc90a4"></a> `00bc90a4` | `27 4b 02 94` | bl 0x00c5bd40 | `UNCONDITIONAL_CALL`
<a id="insn-00bc90a8"></a> `00bc90a8` | `f6 03 1f 2a` | mov w22,wzr | `FALL_THROUGH`
<a id="insn-00bc90ac"></a> `00bc90ac` | `02 00 00 14` | b 0x00bc90b4 | `UNCONDITIONAL_JUMP`
<a id="insn-00bc90b0"></a> `00bc90b0` | `36 00 80 52` | mov w22,#0x1 | `FALL_THROUGH`
<a id="insn-00bc90b4"></a> `00bc90b4` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-00bc90b8"></a> `00bc90b8` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bc90bc"></a> `00bc90bc` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00bc90c0"></a> `00bc90c0` | `08 5d 40 f9` | ldr x8,[x8, #0xb8] | `FALL_THROUGH`
<a id="insn-00bc90c4"></a> `00bc90c4` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bc90c8"></a> `00bc90c8` | `53 00 00 b4` | cbz x19,0x00bc90d0 | `CONDITIONAL_JUMP`
<a id="insn-00bc90cc"></a> `00bc90cc` | `76 12 00 39` | strb w22,[x19, #0x4] | `FALL_THROUGH`
<a id="insn-00bc90d0"></a> `00bc90d0` | `ff 1e 00 72` | tst w23,#0xff | `FALL_THROUGH`
<a id="insn-00bc90d4"></a> `00bc90d4` | `e8 07 9f 1a` | cset w8,ne | `FALL_THROUGH`
<a id="insn-00bc90d8"></a> `00bc90d8` | `00 01 16 0a` | and w0,w8,w22 | `FALL_THROUGH`
<a id="insn-00bc90dc"></a> `00bc90dc` | `fd 7b 43 a9` | ldp x29,x30,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bc90e0"></a> `00bc90e0` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bc90e4"></a> `00bc90e4` | `f6 57 41 a9` | ldp x22,x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bc90e8"></a> `00bc90e8` | `f7 07 44 f8` | ldr x23,[sp], #0x40 | `FALL_THROUGH`
<a id="insn-00bc90ec"></a> `00bc90ec` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bc8ffc`](#insn-00bc8ffc) 範囲 `[['00bc8ffc', '00bc903b']]`
  - `CONDITIONAL_JUMP` [`00bc9038`](#insn-00bc9038) → [`00bc90dc`](#insn-00bc90dc)
  - `FALL_THROUGH` [`00bc9038`](#insn-00bc9038) → [`00bc903c`](#insn-00bc903c)
- ブロック [`00bc903c`](#insn-00bc903c) 範囲 `[['00bc903c', '00bc906f']]`
  - `CONDITIONAL_JUMP` [`00bc906c`](#insn-00bc906c) → [`00bc90b0`](#insn-00bc90b0)
  - `FALL_THROUGH` [`00bc906c`](#insn-00bc906c) → [`00bc9070`](#insn-00bc9070)
- ブロック [`00bc9070`](#insn-00bc9070) 範囲 `[['00bc9070', '00bc90af']]`
  - `UNCONDITIONAL_JUMP` [`00bc90ac`](#insn-00bc90ac) → [`00bc90b4`](#insn-00bc90b4)
- ブロック [`00bc90b0`](#insn-00bc90b0) 範囲 `[['00bc90b0', '00bc90b3']]`
  - `FALL_THROUGH` [`00bc90b0`](#insn-00bc90b0) → [`00bc90b4`](#insn-00bc90b4)
- ブロック [`00bc90b4`](#insn-00bc90b4) 範囲 `[['00bc90b4', '00bc90cb']]`
  - `CONDITIONAL_JUMP` [`00bc90c8`](#insn-00bc90c8) → [`00bc90d0`](#insn-00bc90d0)
  - `FALL_THROUGH` [`00bc90c8`](#insn-00bc90c8) → [`00bc90cc`](#insn-00bc90cc)
- ブロック [`00bc90cc`](#insn-00bc90cc) 範囲 `[['00bc90cc', '00bc90cf']]`
  - `FALL_THROUGH` [`00bc90cc`](#insn-00bc90cc) → [`00bc90d0`](#insn-00bc90d0)
- ブロック [`00bc90d0`](#insn-00bc90d0) 範囲 `[['00bc90d0', '00bc90db']]`
  - `FALL_THROUGH` [`00bc90d8`](#insn-00bc90d8) → [`00bc90dc`](#insn-00bc90dc)
- ブロック [`00bc90dc`](#insn-00bc90dc) 範囲 `[['00bc90dc', '00bc90ef']]`

## 命令位置別の参照

- [`00bc8ffc`](#insn-00bc8ffc) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc9000`](#insn-00bc9000) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc9004`](#insn-00bc9004) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc9008`](#insn-00bc9008) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc9020`](#insn-00bc9020) → [`00c5c120`](../00c5c/00c5c120.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5c120` · 推定シンボル `None` · 推定型 `None`
- [`00bc9034`](#insn-00bc9034) → [`00bc90f0`](../00bc9/00bc90f0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bc90f0` · 推定シンボル `None` · 推定型 `None`
- [`00bc9038`](#insn-00bc9038) → [`00bc90dc`](#insn-00bc90dc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc9040`](#insn-00bc9040) → `01127610`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bc9050`](#insn-00bc9050) → [`00497da8`](../00497/00497da8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00497da8` · 推定シンボル `None` · 推定型 `None`
- [`00bc906c`](#insn-00bc906c) → [`00bc90b0`](#insn-00bc90b0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc9098`](#insn-00bc9098) → `002a0cc9`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bc909c`](#insn-00bc909c) → `002aa990`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bc90a4`](#insn-00bc90a4) → [`00c5bd40`](../00c5b/00c5bd40.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5bd40` · 推定シンボル `None` · 推定型 `None`
- [`00bc90ac`](#insn-00bc90ac) → [`00bc90b4`](#insn-00bc90b4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc90c8`](#insn-00bc90c8) → [`00bc90d0`](#insn-00bc90d0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc90dc`](#insn-00bc90dc) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc90e0`](#insn-00bc90e0) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc90e4`](#insn-00bc90e4) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bc8ffc`](#insn-00bc8ffc)

~~~json
{
  "source": "00bc8ffc",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc9000`](#insn-00bc9000)

~~~json
{
  "source": "00bc9000",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc9004`](#insn-00bc9004)

~~~json
{
  "source": "00bc9004",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc9008`](#insn-00bc9008)

~~~json
{
  "source": "00bc9008",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc9020`](#insn-00bc9020)

~~~json
{
  "source": "00bc9020",
  "target": "00c5c120",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bc9034`](#insn-00bc9034)

~~~json
{
  "source": "00bc9034",
  "target": "00bc90f0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bc9038`](#insn-00bc9038)

~~~json
{
  "source": "00bc9038",
  "target": "00bc90dc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc9040`](#insn-00bc9040)

~~~json
{
  "source": "00bc9040",
  "target": "01127610",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127610",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bc9050`](#insn-00bc9050)

~~~json
{
  "source": "00bc9050",
  "target": "00497da8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bc906c`](#insn-00bc906c)

~~~json
{
  "source": "00bc906c",
  "target": "00bc90b0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc9098`](#insn-00bc9098)

~~~json
{
  "source": "00bc9098",
  "target": "002a0cc9",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a0cc9",
  "offset": 0,
  "size": 55,
  "datatype": "string",
  "bytes": "52656d6f746520436f6e6669673a204661696c656420746f2072657472696576",
  "capture_start": "002a0cc9",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00bc909c`](#insn-00bc909c)

~~~json
{
  "source": "00bc909c",
  "target": "002aa990",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002aa990",
  "offset": 0,
  "size": 8,
  "datatype": "string",
  "bytes": "626f6f6c65616e00",
  "capture_start": "002aa990",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bc90a4`](#insn-00bc90a4)

~~~json
{
  "source": "00bc90a4",
  "target": "00c5bd40",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bc90ac`](#insn-00bc90ac)

~~~json
{
  "source": "00bc90ac",
  "target": "00bc90b4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc90c8`](#insn-00bc90c8)

~~~json
{
  "source": "00bc90c8",
  "target": "00bc90d0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc90dc`](#insn-00bc90dc)

~~~json
{
  "source": "00bc90dc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc90e0`](#insn-00bc90e0)

~~~json
{
  "source": "00bc90e0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc90e4`](#insn-00bc90e4)

~~~json
{
  "source": "00bc90e4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
