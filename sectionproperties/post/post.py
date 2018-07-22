import matplotlib.pyplot as plt


def setup_plot(ax, pause):
    """Exectues code required to set up a matplotlib figure.

    :param ax: Axes object on which to plot
    :type ax: :class:`matplotlib.axes.Axes`
    :param bool pause: If set to true, the figure pauses the script until
        the window is closed. If set to false, the script continues
        immediately after the window is rendered.
    """

    if not pause:
        plt.ion()
        plt.show()

    ax.set_aspect("equal")


def finish_plot(ax, pause, title=''):
    """Executes code required to finish a matplotlib figure.

    :param ax: Axes object on which to plot
    :param bool pause: If set to true, the figure pauses the script until
        the window is closed. If set to false, the script continues
        immediately after the window is rendered.
    :param string title: Plot title
    """

    ax.set_title(title)

    if pause:
        plt.show()
    else:
        plt.draw()
        plt.pause(0.001)


def print_results(cross_section, fmt):
    """Prints the results that have been calculated to the terminal.

    :param cross_section: Structural cross-section object
    :type section_properties:
        :class:`sectionproperties.cross_section.CrossSection`
    :param string fmt: Number format
    """

    area = cross_section.get_area()
    if area is not None:
        print("Section Properties:")
        print("Area\t = {:>{fmt}}".format(area, fmt=fmt))

    (qx, qy) = cross_section.get_q()
    if qx is not None:
        print("Qx\t = {:>{fmt}}".format(qx, fmt=fmt))
        print("Qy\t = {:>{fmt}}".format(qy, fmt=fmt))

    (cx, cy) = cross_section.get_c()
    if cx is not None:
        print("cx\t = {:>{fmt}}".format(cx, fmt=fmt))
        print("cy\t = {:>{fmt}}".format(cy, fmt=fmt))

    (ixx_g, iyy_g, ixy_g) = cross_section.get_ig()
    if ixx_g is not None:
        print("Ixx_g\t = {:>{fmt}}".format(ixx_g, fmt=fmt))
        print("Iyy_g\t = {:>{fmt}}".format(iyy_g, fmt=fmt))
        print("Ixy_g\t = {:>{fmt}}".format(ixy_g, fmt=fmt))

    (ixx_c, iyy_c, ixy_c) = cross_section.get_ic()
    if ixx_c is not None:
        print("Ixx_c\t = {:>{fmt}}".format(ixx_c, fmt=fmt))
        print("Iyy_c\t = {:>{fmt}}".format(iyy_c, fmt=fmt))
        print("Ixy_c\t = {:>{fmt}}".format(ixy_c, fmt=fmt))

    (zxx_plus, zxx_minus, zyy_plus, zyy_minus) = cross_section.get_z()
    if zxx_plus is not None:
        print("Zxx+\t = {:>{fmt}}".format(zxx_plus, fmt=fmt))
        print("Zxx-\t = {:>{fmt}}".format(zxx_minus, fmt=fmt))
        print("Zyy+\t = {:>{fmt}}".format(zyy_plus, fmt=fmt))
        print("Zyy-\t = {:>{fmt}}".format(zyy_minus, fmt=fmt))

    (rx, ry) = cross_section.get_rc()
    if rx is not None:
        print("rx\t = {:>{fmt}}".format(rx, fmt=fmt))
        print("ry\t = {:>{fmt}}".format(ry, fmt=fmt))

    phi = cross_section.get_phi()
    (i11_c, i22_c) = cross_section.get_ip()
    if phi is not None:
        print("phi\t = {:>{fmt}}".format(phi, fmt=fmt))
        print("I11_c\t = {:>{fmt}}".format(i11_c, fmt=fmt))
        print("I22_c\t = {:>{fmt}}".format(i22_c, fmt=fmt))

    (z11_plus, z11_minus, z22_plus, z22_minus) = cross_section.get_zp()
    if z11_plus is not None:
        print("Z11+\t = {:>{fmt}}".format(z11_plus, fmt=fmt))
        print("Z11-\t = {:>{fmt}}".format(z11_minus, fmt=fmt))
        print("Z22+\t = {:>{fmt}}".format(z22_plus, fmt=fmt))
        print("Z22-\t = {:>{fmt}}".format(z22_minus, fmt=fmt))

    (r11, r22) = cross_section.get_rp()
    if r11 is not None:
        print("r11\t = {:>{fmt}}".format(r11, fmt=fmt))
        print("r22\t = {:>{fmt}}".format(r22, fmt=fmt))

    j = cross_section.get_j()
    if j is not None:
        print("J\t = {:>{fmt}}".format(j, fmt=fmt))

    gamma = cross_section.get_gamma()
    if gamma is not None:
        print("Iw\t = {:>{fmt}}".format(gamma, fmt=fmt))

    (x_se, y_se) = cross_section.get_sc_e()
    if x_se is not None:
        print("x_se\t = {:>{fmt}}".format(x_se, fmt=fmt))
        print("y_se\t = {:>{fmt}}".format(y_se, fmt=fmt))

    (x_st, y_st) = cross_section.get_sc_t()
    if x_se is not None:
        print("x_st\t = {:>{fmt}}".format(x_st, fmt=fmt))
        print("y_st\t = {:>{fmt}}".format(y_st, fmt=fmt))

    (x1_se, y2_se) = cross_section.get_sc_p_e()
    if x1_se is not None:
        print("x1_se\t = {:>{fmt}}".format(x1_se, fmt=fmt))
        print("y2_se\t = {:>{fmt}}".format(y2_se, fmt=fmt))

    (A_sx, A_sy, _) = cross_section.get_As()
    if A_sx is not None:
        print("A_sx\t = {:>{fmt}}".format(A_sx, fmt=fmt))
        print("A_sy\t = {:>{fmt}}".format(A_sy, fmt=fmt))

    (A_s11, A_s22) = cross_section.get_As_p()
    if A_sx is not None:
        print("A_s11\t = {:>{fmt}}".format(A_s11, fmt=fmt))
        print("A_s22\t = {:>{fmt}}".format(A_s22, fmt=fmt))

    # if section_properties.x_pc is not None:
    #     print("x_pc\t = {:>{fmt}}".format(section_properties.x_pc, fmt=fmt))
    #     print("y_pc\t = {:>{fmt}}".format(section_properties.y_pc, fmt=fmt))
    #
    # if section_properties.Sxx is not None:
    #     print("Sxx\t = {:>{fmt}}".format(section_properties.Sxx, fmt=fmt))
    #     print("Syy\t = {:>{fmt}}".format(section_properties.Syy, fmt=fmt))
    #     print("SF_xx+\t = {:>{fmt}}".format(section_properties.SF_xx_plus,
    #                                         fmt=fmt))
    #     print("SF_xx-\t = {:>{fmt}}".format(section_properties.SF_xx_minus,
    #                                         fmt=fmt))
    #     print("SF_yy+\t = {:>{fmt}}".format(section_properties.SF_yy_plus,
    #                                         fmt=fmt))
    #     print("SF_yy-\t = {:>{fmt}}".format(section_properties.SF_yy_minus,
    #                                         fmt=fmt))
    #
    # if section_properties.x1_pc is not None:
    #     print("x1_pc\t = {:>{fmt}}".format(section_properties.x1_pc, fmt=fmt))
    #     print("y2_pc\t = {:>{fmt}}".format(section_properties.y2_pc, fmt=fmt))
    #
    # if section_properties.S11 is not None:
    #     print("S11\t = {:>{fmt}}".format(section_properties.S11, fmt=fmt))
    #     print("S22\t = {:>{fmt}}".format(section_properties.S22, fmt=fmt))
    #     print("SF_11+\t = {:>{fmt}}".format(section_properties.SF_11_plus,
    #                                         fmt=fmt))
    #     print("SF_11-\t = {:>{fmt}}".format(section_properties.SF_11_minus,
    #                                         fmt=fmt))
    #     print("SF_22+\t = {:>{fmt}}".format(section_properties.SF_22_plus,
    #                                         fmt=fmt))
    #     print("SF_22-\t = {:>{fmt}}".format(section_properties.SF_22_minus,
    #                                         fmt=fmt))

    print("\n")