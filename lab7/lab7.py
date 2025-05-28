import dearpygui.dearpygui as dpg
from Geometry.Shape import Shape
from Geometry.rectangle import Rectangle
from Geometry.triangle import Triangle
from Geometry.trapezoid import Trapezoid
from docx import Document

def update_form(sender, app_data, user_data):
    dpg.delete_item("param_group", children_only=True)

    figure = dpg.get_value("figure_combo")

    if figure == "Rectangle":
        for param in ["Width", "Height"]:
            with dpg.group(parent="param_group"):
                dpg.add_text(param)
                dpg.add_input_float(tag=f"input_{param}", default_value=0.0)

    elif figure == "Triangle":
        for param in ["Side a", "Side b", "Side c"]:
            with dpg.group(parent="param_group"):
                dpg.add_text(param)
                dpg.add_input_float(tag=f"input_{param}", default_value=0.0)

    elif figure == "Trapezoid":
        for param in ["Base a", "Base b", "Side c", "Side d", "Height"]:
            with dpg.group(parent="param_group"):
                dpg.add_text(param)
                dpg.add_input_float(tag=f"input_{param}", default_value=0.0)


def calculate_callback(sender, app_data, user_data):
    figure = dpg.get_value("figure_combo")
    result_text = ""

    try:
        if figure == "Rectangle":
            width = dpg.get_value("input_Width")
            height = dpg.get_value("input_Height")
            rect = Rectangle(width, height)
            area = rect.area()
            r_in = rect.inscribed_circle_radius()
            r_out = rect.circumscribed_circle_radius()
            params = f"Width={width}, Height={height}"

        elif figure == "Triangle":
            a = dpg.get_value("input_Side a")
            b = dpg.get_value("input_Side b")
            c = dpg.get_value("input_Side c")
            tri = Triangle(a, b, c)
            area = tri.area()
            r_in = tri.inscribed_circle_radius()
            r_out = tri.circumscribed_circle_radius()
            params = f"a={a}, b={b}, c={c}"

        elif figure == "Trapezoid":
            a = dpg.get_value("input_Base a")
            b = dpg.get_value("input_Base b")
            c = dpg.get_value("input_Side c")
            d = dpg.get_value("input_Side d")
            h = dpg.get_value("input_Height")
            trap = Trapezoid(a, b, c, d, h)
            area = trap.area()
            r_in = trap.inscribed_circle_radius()
            r_out = trap.circumscribed_circle_radius()
            params = f"a={a}, b={b}, c={c}, d={d}, h={h}"

        result_text = (
            f"Figure: {figure}\n"
            f"Parameters: {params}\n"
            f"Area: {area:.3f}\n"
            f"Inscribed circle radius: {r_in if r_in is not None else 'N/A'}\n"
            f"Circumscribed circle radius: {r_out if r_out is not None else 'N/A'}"
        )

        global last_result
        last_result = {
            "Figure": figure,
            "Parameters": params,
            "Area": area,
            "Inscribed circle radius": r_in if r_in is not None else "N/A",
            "Circumscribed circle radius": r_out if r_out is not None else "N/A"
        }
    except Exception as e:
        result_text = f"Error: {str(e)}"

    dpg.set_value("result_text", result_text)


def save_to_word_callback(sender, app_data, user_data):
    path = "result.docx"
    doc = Document()

    for key, value in last_result.items():
        doc.add_paragraph(f"{key}: {value}")

    doc.save(path)
    dpg.set_value("result_text", f"Result saved to {path}")


#GUI
dpg.create_context()
dpg.create_viewport(title="Geometric Shapes", width=650, height=500)

last_result = {}

with dpg.window(label="Geometric Shapes", width=650, height=500):
    dpg.add_text("Select a shape:")
    dpg.add_combo(["Rectangle", "Triangle", "Trapezoid"], default_value="Rectangle", tag="figure_combo",
                  callback=update_form)

    with dpg.group(tag="param_group"):
        pass

    dpg.add_button(label="Calculate", callback=calculate_callback)
    dpg.add_text("", tag="result_text")
    dpg.add_button(label="Save to Word", callback=save_to_word_callback)

update_form(None, None, None)

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
