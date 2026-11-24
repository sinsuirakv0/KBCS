# 00bce4fc

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bcd508`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcd/00bcd508.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0081.md#compare-344102d9fc829dd5d378d16690b73fc6)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bce4fc",
  "name": "_ZN8firebase4auth14SetEmulatorJniEPNS0_8AuthDataEPKcj",
  "size": 128,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "69521913cded4f61ea8f83b9047d34fe060c354701a9b3085c7a54517a18a5a7",
  "source_text_sha256": "69521913cded4f61ea8f83b9047d34fe060c354701a9b3085c7a54517a18a5a7",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bce4fc",
        "00bce57b"
      ]
    ],
    "bytes_sha256": "1aee58386123b1b24534b45a60f97e436441dac0f812b5c660461229caaae319",
    "instruction_count": 32,
    "instruction_bytes": 128,
    "body_bytes": 128,
    "indirect": 2,
    "unresolved": 2
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [0057504c](../00575/0057504c.md)
- [00c5c000](../00c5c/00c5c000.md)
- [00c5c120](../00c5c/00c5c120.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 487 bytes

~~~c

void _ZN8firebase4auth14SetEmulatorJniEPNS0_8AuthDataEPKcj
               (undefined8 *param_1,undefined8 param_2,undefined4 param_3)

{
  long *plVar1;
  undefined8 uVar2;
  
  plVar1 = (long *)_ZNK8firebase3App9GetJNIEnvEv(*param_1);
  uVar2 = (**(code **)(*plVar1 + 0x538))(plVar1,param_2);
  FUN_0057504c(plVar1,param_1[0x3f],DAT_01127848,uVar2,param_3);
  (**(code **)(*plVar1 + 0xb8))(plVar1,uVar2);
  _ZN8firebase4util26CheckAndClearJniExceptionsEP7_JNIEnv(plVar1);
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bce4fc"></a> `00bce4fc` | `f6 57 bd a9` | stp x22,x21,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00bce500"></a> `00bce500` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bce504"></a> `00bce504` | `fd 7b 02 a9` | stp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bce508"></a> `00bce508` | `fd 83 00 91` | add x29,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00bce50c"></a> `00bce50c` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00bce510"></a> `00bce510` | `00 00 40 f9` | ldr x0,[x0] | `FALL_THROUGH`
<a id="insn-00bce514"></a> `00bce514` | `f3 03 02 2a` | mov w19,w2 | `FALL_THROUGH`
<a id="insn-00bce518"></a> `00bce518` | `f5 03 01 aa` | mov x21,x1 | `FALL_THROUGH`
<a id="insn-00bce51c"></a> `00bce51c` | `01 37 02 94` | bl 0x00c5c120 | `UNCONDITIONAL_CALL`
<a id="insn-00bce520"></a> `00bce520` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00bce524"></a> `00bce524` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00bce528"></a> `00bce528` | `f6 03 00 aa` | mov x22,x0 | `FALL_THROUGH`
<a id="insn-00bce52c"></a> `00bce52c` | `08 9d 42 f9` | ldr x8,[x8, #0x538] | `FALL_THROUGH`
<a id="insn-00bce530"></a> `00bce530` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bce534"></a> `00bce534` | `c8 2a 00 b0` | adrp x8,0x1127000 | `FALL_THROUGH`
<a id="insn-00bce538"></a> `00bce538` | `81 fe 40 f9` | ldr x1,[x20, #0x1f8] | `FALL_THROUGH`
<a id="insn-00bce53c"></a> `00bce53c` | `02 25 44 f9` | ldr x2,[x8, #0x848] | `FALL_THROUGH`
<a id="insn-00bce540"></a> `00bce540` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00bce544"></a> `00bce544` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00bce548"></a> `00bce548` | `e3 03 14 aa` | mov x3,x20 | `FALL_THROUGH`
<a id="insn-00bce54c"></a> `00bce54c` | `e4 03 13 2a` | mov w4,w19 | `FALL_THROUGH`
<a id="insn-00bce550"></a> `00bce550` | `bf 9a e6 97` | bl 0x0057504c | `UNCONDITIONAL_CALL`
<a id="insn-00bce554"></a> `00bce554` | `c8 02 40 f9` | ldr x8,[x22] | `FALL_THROUGH`
<a id="insn-00bce558"></a> `00bce558` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00bce55c"></a> `00bce55c` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00bce560"></a> `00bce560` | `08 5d 40 f9` | ldr x8,[x8, #0xb8] | `FALL_THROUGH`
<a id="insn-00bce564"></a> `00bce564` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bce568"></a> `00bce568` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bce56c"></a> `00bce56c` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bce570"></a> `00bce570` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00bce574"></a> `00bce574` | `f6 57 c3 a8` | ldp x22,x21,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00bce578"></a> `00bce578` | `a2 36 02 14` | b 0x00c5c000 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bce4fc`](#insn-00bce4fc) 範囲 `[['00bce4fc', '00bce57b']]`

## 命令位置別の参照

- [`00bce4fc`](#insn-00bce4fc) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bce500`](#insn-00bce500) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bce504`](#insn-00bce504) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bce51c`](#insn-00bce51c) → [`00c5c120`](../00c5c/00c5c120.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5c120` · 推定シンボル `None` · 推定型 `None`
- [`00bce53c`](#insn-00bce53c) → `01127848`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bce550`](#insn-00bce550) → [`0057504c`](../00575/0057504c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0057504c` · 推定シンボル `None` · 推定型 `None`
- [`00bce568`](#insn-00bce568) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bce56c`](#insn-00bce56c) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bce578`](#insn-00bce578) → [`00c5c000`](../00c5c/00c5c000.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5c000` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bce4fc`](#insn-00bce4fc)

~~~json
{
  "source": "00bce4fc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bce500`](#insn-00bce500)

~~~json
{
  "source": "00bce500",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bce504`](#insn-00bce504)

~~~json
{
  "source": "00bce504",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bce51c`](#insn-00bce51c)

~~~json
{
  "source": "00bce51c",
  "target": "00c5c120",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bce53c`](#insn-00bce53c)

~~~json
{
  "source": "00bce53c",
  "target": "01127848",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127848",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bce550`](#insn-00bce550)

~~~json
{
  "source": "00bce550",
  "target": "0057504c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bce568`](#insn-00bce568)

~~~json
{
  "source": "00bce568",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bce56c`](#insn-00bce56c)

~~~json
{
  "source": "00bce56c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bce578`](#insn-00bce578)

~~~json
{
  "source": "00bce578",
  "target": "00c5c000",
  "target_space": "ram",
  "resolution": "function"
}
~~~
